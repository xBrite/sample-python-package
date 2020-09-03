# xBrite Sample Python Package

This repository contains code and instructions that can be used to quickly
bootstrap a new python package, including code to automatically ensure that
`*.pyx` files will be compiled using cython.

It uses `direnv` to automatically set up a preferred python virtual
environment, and uses that to include support for opinionated code
autoformatting using `black` and `isort`, along with settings for `vscode` to
keep everything in sync. More on these below

## Using this package

- Create a new git repository
  [at Github](https://help.github.com/articles/create-a-repo/), or wherever
  else you prefer.
- Clone the repository to a local directory of your choice, represented below
  as `$MY_REPO_PATH`.
- Get a copy of the files in **this** repository into your new one, but without
  all of the `.git` metadata:

  ```bash
  cd $MY_REPO_PATH
  curl -L https://github.com/xBrite/sample-python-package/tarball/master \
      | tar xz --strip-components=1 -C .
  ```

- Run `init_package.sh` to propagate your own package's name where it needs
  to go.
- Remove the contents of the README and replace with your own documentation
  or placeholders.
- `setup.py` contains a section at the top containing more than a few fields
  that are currently hard-coded to example values. You should change these to
  match your own package.
- There are various `CHANGEME` comments scattered throughout `setup.py` with
  recommendations for how you might want to change the file. The most likely
  of these relate to the use of `cython` and/or `numpy`.

## Additional Setup

- [License your package](https://help.github.com/articles/licensing-a-repository/)
- The `tox` config in `pyproject.toml` is set up for a handful of common test
  scenarios, including building with cython. You may not need all of it.

## direnv

TODO: why direnv?
TODO: link to direnv instructions

## Code autoformatting

Developers can spend weeks arguing over the benefits of tabs vs spaces, or how
all code should be legible within an 80x20 `vim` terminal window. Even with
python's strong `PEP8` recommendations, not everything is covered and code can
easily end up in situations where diffs and pull requests can become cluttered
with unnecessary formatting changes as users forget to trim whitespace,
rearrange the order of their import statements, etc.

This sample package includes support for `vscode` to autoformat as much code as
possible, and includes the `autoformat` script
[described below](#bin-directory) to catch the rest. These work together to
ensure that all code formatting from all contributors matches. Individual
choices from these opinionated formatters may not make everyone happy but they
are a good compromise toward consistency and clean code submitted for review.

The recommended tools are:

- [`black`](https://github.com/psf/black),
  [`autoflake`](https://github.com/myint/autoflake), and
  [`isort`](https://pycqa.github.io/isort/) for python code.
- [`prettier`](https://prettier.io/) for markdown, json, and many other
  formats should you choose to add them.

## `bin` Directory

This directory contains several wrapper scripts intended to make managing code
and builds easier during development, especially when working with cython.

- `autoformat`
  - Runs tools like `black` and `prettier` (if installed) to autoformat all of
    the code in the repository (more expansive than the included vscode
    settings allow for).
    - Note that you will have to install `prettier` yourself if you wish it to
      run.
  - You can adjust the settings for these programs via their respective config
    files, but the point is to have consistent and opinionated autoformatting
    so diffs and pull requests against your code present the least amount of
    change as possible, so actual code changes stand out more.
- `lint`
  - Wrapper around both `flake8` and `mypy`.
- `clean`
  - Removes any leftover build files.
- `build`
  - Wrapper around `clean` and `setup.py build_ext` to build a cython package.
