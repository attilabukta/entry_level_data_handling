## Introduction

This is a skeleton project used as an init commit for a general Python project, using `pipenv` as a package manager

## Pipenv setup

### Install pipenv for your OS

On every type of OS you can use pip to install Pipenv as a global package with the following 
command:
```bash
pip install pipenv
```
But the recommended way is to use your OS specific package manager. On MacOS, use Homebrew by
running:
```bash
brew install pipenv
```    
On Linux distributions, most of the built-in package managers can acquire this package, but it
depends on your specific distribution, some examples:
```bash
sudo apt install pipenv  # Debian-based systems
sudo dnf install pipenv  # Fedora-based systems
sudo pacman -S python-pipenv  # Arch-based systems
```  
For Windows users pip is the recommended option on the main site, but it could also be installed
using chocolatey, a package manager for Windows.

For more information on installation visit the official documentation.

### Navigate to the project folder

Shell navigation to the project is going to be necessary to use Pipenv. On most OS you can
simply type the following into your terminal:
```bash
cd path/to/your/project
```

### Install dependencies

```bash
pipenv install --dev
```
Using the above command you create a virtual environment if you don't have one on your machine
yet for the project, and then install all the packages specified in your `Pipfile`. 
Adding the `--dev` flag also installs dev packages, which is recommended for development.

### Running commands

To run anything in pipenv you need to use the following command:
```bash
pipenv run {your_command}
```
There are some command shortcuts added to the project, such as `start`, `lint` or `test`.
Consult the pipfile for details about these commands.

## Testing

For testing this skeleton contains `pytest`, a lightweight testing library for python.

## Linting

The included linting package is `pylint`. there is a generic `.pylintrc` that I found works best for me, this might need modification based on preference.
It mostly follows PEP8 standards, but it was modified at a few places to be more forgiving.

## Githooks

The `python-githooks` package is added to configure hooks.
`.githooks.ini` is fairly self-explanatory, but to sum up - by the current configuration
Lint is run on every commit and tests on every push. If Linting doesn't return a perfect score,
or if any of the tests fail, the respective action is rejected.
To enable the hooks locally you need to run the following command (assuming you are using pipenv):
```bash
pipenv run githooks
```
