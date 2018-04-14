# xBrite Sample Python Package

This repository contains code and instructions that can be used to quickly
bootstrap a new python package, including code to automatically ensure that
`*.pyx` files will be compiled using cython.

# Using this package 

* Create a new git repository
  [at Github](https://help.github.com/articles/create-a-repo/), or wherever
  else you prefer.
* Clone the repository to a local directory of your choice, represented below
  as `$MY_REPO_PATH`.
* Get a copy of the files in **this** repository into your new one, but without
  all of the `.git` metadata:
    ```bash
    cd $MY_REPO_PATH
    curl -L https://github.com/xBrite/sample-python-package/tarball/master \
        | tar xz --strip-components=1 -C .
    ```
* Run `init_package.sh` to propagate your own package's name where it needs
  to go.
* Remove the contents of the README and replace with your own documentation
  or placeholders.
* `setup.py` contains a section at the top containing more than a few fields
  that are currently hard-coded to example values. You should probably change
  these.
* There are various `CHANGEME` comments scattered throughout `setup.py` with
  recommendations for how you might want to change the file. The most likely
  of these relate to the use of `cython` and/or `numpy`.

# Additional Setup

* [License your package](https://help.github.com/articles/licensing-a-repository/)
* The `tox.ini` config is set up for a handful of common test scenarios,
  including building with cython. You may not need all of it.

# `bin` Directory

This directory contains two scripts, `build` and `clean`, which are intended to
make managing cython builds slightly easier during development. Feel free to
delete these if you're not using cython.
