# Cookie Cutter: Poetry Python Project

A highly opinionated [cookiecutter](https://github.com/cookiecutter/cookiecutter) for creating a 
Python project with the following enabled:

- `poetry` for project management
- `tox` for task management (test, lint, coverage)
- `coverage` configuration with support for multiple python versions
- CI configuration
    - GitHub workflows
- `pre-commit` configuration, with the following hooks
    - `black` configuration for code style
    - `flake8` for code quality assurance (flake8-annotations plugin enabled)
    - `isort` for import ordering
    - `trailing-whitespace`
    - `end-of-file-fixer`
    - `debug-statements`
- Module level `__version__` variable using [importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html) 
or [importlib_metadata](https://importlib-metadata.readthedocs.io/en/latest/).
 
#### Additional Files Generated
You can refer to the template's [hooks][hooks] for details of urls used.

- `.gitignore`: A default git ignore file is created using [GitHub ignore templates](https://github.com/github/gitignore/)
- `LICENSE`: If project chooses an [SPDX](https://spdx.org/licenses/) license, a 
 LICENCE file is generated using the [GitHub Licence API](https://docs.github.com/en/rest/reference/licenses).
- Default `README.md` and `CONTRIBUTING.md` files.

#### Requirements
This cookiecutter's hooks makes use of the following when generating the project.
- [Poetry](https://python-poetry.org/docs)
- [Python Requests](https://requests.readthedocs.io/en/master/) (A dependency of cookiecutter)

You can install `poetry` as shown here using [pipx](https://pipxproject.github.io/pipx/).
```sh
pipx install poetry
```

### Example Usage
```sh
cookiecutter https://github.com/abn/cookiecutter-python-project.git
```

This should produce an output similar to this.

```console
project [project-name]: acme-foo-bar
directory_name [acme-foo-bar]: python-acme-foo-bar
description [My Amazing Project]: ACME's new foo, now with bar.
author_name [Turanga Leela]: 
author_email [turanga.leela@planetexpress.com]: 
namespace [acme.foo.bar]: 
Select minimum_python_version:
1 - 3.6
2 - 3.7
3 - 3.8
4 - 3.9
Choose from 1, 2, 3, 4 [1]: 2
Select license:
1 - MIT
2 - Apache-2.0
3 - AGPL-3.0
4 - MPL-2.0
5 - BSD-3-Clause
6 - GPL-3.0
7 - LGPL-3.0
8 - Proprietary
Choose from 1, 2, 3, 4, 5, 6, 7, 8 [1]: 1
Select ci:
1 - none
2 - github
Choose from 1, 2 [1]: 2
INFO: Using poetry version 1.1.0b2
INFO: Generating .gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/Diff.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/Emacs.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/Vim.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/JetBrains.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/Windows.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/Linux.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Global/macOS.gitignore
INFO: Fetching https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
INFO: Generating LICENSE file
INFO: Fetching https://api.github.com/licenses/MIT
INFO: Writing default __init__.py file
INFO: Executing command: poetry add --lock importlib-metadata --python '<3.8'
Creating virtualenv acme-foo-bar in /tmp/python-acme-foo-bar/.venv
Using version ^1.7.0 for importlib-metadata

Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file
INFO: Executing command: poetry add --lock -D pre-commit
Using version ^2.7.1 for pre-commit

Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file
INFO: Executing command: poetry add --lock -D tox pytest pytest-cov
Using version ^3.20.0 for tox
Using version ^6.0.1 for pytest
Using version ^2.10.1 for pytest-cov

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file
INFO: Executing command: poetry add --lock -D coverage -E toml
Using version ^5.2.1 for coverage

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file
```
