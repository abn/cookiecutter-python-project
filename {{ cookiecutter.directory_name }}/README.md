{% if cookiecutter.license != "Proprietary" -%}
[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.project }})](https://pypi.org/project/{{ cookiecutter.project }}/)
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project }})](https://pypi.org/project/{{ cookiecutter.project }}/)
[![Python Wheel](https://img.shields.io/pypi/wheel/{{ cookiecutter.project }})](https://pypi.org/project/{{ cookiecutter.project }}/)
{% endif -%}
[![License](https://img.shields.io/badge/License-{{ cookiecutter.license.replace('-','') }}-{{ 'red' if cookiecutter.license == 'Proprietary' else 'green' }}.svg)](https://opensource.org/licenses/{{ cookiecutter.license }})
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code Quality: flake8](https://img.shields.io/badge/code%20quality-flake8-000000.svg)](https://gitlab.com/pycqa/flake8)

# {{ cookiecutter.project }}
{{ cookiecutter.description }}

## Contributing
Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to
contribute to this project.
