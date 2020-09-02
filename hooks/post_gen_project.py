import re
import shutil
import subprocess
import sys

from pathlib import Path

import requests

LICENCE = "{{ cookiecutter.license }}"
IS_PROPRIETARY = LICENCE == "Proprietary"

MIN_PYTHON_VERSION = "{{ cookiecutter.minimum_python_version }}"
NAMESPACE = "{{ cookiecutter.namespace }}"
SRC_DIR = Path("src").joinpath(NAMESPACE.replace(".", "/"))
SRC_DIR.mkdir(parents=True)

INIT_FILE_CONTENT = """try:
    from importlib.metadata import version as importlib_metadata_version
except ImportError:
    from importlib_metadata import version as importlib_metadata_version

__version__ = importlib_metadata_version("{{ cookiecutter.project }}")

"""

IGNORES = [
    "https://raw.githubusercontent.com/github/gitignore/master/Global/Diff.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/Emacs.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/Vim.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/JetBrains.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/Windows.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/Linux.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Global/macOS.gitignore",
    "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore",
]

REMOVE_PATHS = [
    '{% if cookiecutter.ci != "github" %}.github{% endif %}'.strip(),
]
if IS_PROPRIETARY:
    REMOVE_PATHS.append(".github/workflows/release.yml")

POETRY_VERSION_REGEX = re.compile(r"^Poetry version (?P<version>(\d+\.){2}\w+)$")


def get_poetry_version():
    # poor person's version check
    proc = subprocess.run("poetry --version", shell=True, capture_output=True)
    if proc.returncode != 0:
        print("CRITICAL: Unable to execute poetry command, please install poetry.")
        sys.exit(-1)

    output = proc.stdout.decode().strip()
    match = POETRY_VERSION_REGEX.match(output)
    if match:
        version = match.group("version")
        print(f"INFO: Using poetry version {version}")
        return tuple(match.group("version").split("."))
    else:
        print(f"WARN: Unable to determine poetry version from '{output}'")
    return "0", "0", "0"


POETRY_VERSION = get_poetry_version()


def run(command):
    try:
        print(f"INFO: Executing command: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command execution failed: {e}")


def cleanup():
    for path in REMOVE_PATHS:
        if not path.strip():
            continue

        path = Path(path.strip())

        if not path.exists():
            print("NOT EXISTS", path.resolve(strict=False).as_posix())
            continue

        print(f"INFO: Removing unused file/directory: {path.as_posix()}")

        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)


def generate_gitignore():
    with Path(".gitignore").open("a") as gitignore:
        print("INFO: Generating .gitignore")
        for ignore in IGNORES:
            try:
                print("INFO: Fetching {}".format(ignore))
                with requests.get(ignore) as response:
                    gitignore.write(f"## source: {ignore}")
                    gitignore.write(response.text)
                    gitignore.write("")
            except requests.exceptions.HTTPError:
                pass
        gitignore.write("## source: custom ignores")
        gitignore.write(".coverage")
        gitignore.write("")


def generate_license_file():
    if not IS_PROPRIETARY:
        print("INFO: Generating LICENSE file")
        try:
            url = f"https://api.github.com/licenses/{LICENCE}"
            print("INFO: Fetching {}".format(url))
            with requests.get(url) as response:
                data = response.json()
                with Path("LICENSE").open("w") as f:
                    f.write(data.get("body", ""))
        except requests.exceptions.HTTPError:
            pass
    else:
        print("INFO: Skipping generation of LICENCE since project is proprietary")


def generate_init_file():
    print("INFO: Writing default __init__.py file")
    with SRC_DIR.joinpath("__init__.py").open("w") as init_file:
        init_file.write(INIT_FILE_CONTENT)


def add_dependencies():
    add_command = "poetry add"
    if tuple(map(int, POETRY_VERSION[:-1])) >= (1, 1):
        # lock only
        add_command = f"{add_command} --lock"
    else:
        print(
            "WARN: Poetry version does not support lock only dependency addition, this"
            " will create a project virtual environment."
        )

    if MIN_PYTHON_VERSION in {"3.6", "3.7"}:
        run(f"{add_command} importlib-metadata --python '<3.8'")

    if MIN_PYTHON_VERSION == "3.6":
        run(f"{add_command} -D pre-commit --python '>=3.6.1'")
    else:
        run(f"{add_command} -D pre-commit")

    run(f"{add_command} -D tox pytest pytest-cov")
    run(f"{add_command} -D coverage -E toml")


def main():
    generate_gitignore()
    generate_license_file()
    generate_init_file()
    add_dependencies()
    cleanup()


main()
