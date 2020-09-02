#!/usr/bin/env python
"""
A setuptools based setup module generated from the xBrite Sample Package.

See:
* https://github.com/xBrite/sample-python-package
* https://packaging.python.org/en/latest/distributing.html
* https://github.com/pypa/sampleproject
"""

import os
import re

# To use a consistent encoding
from codecs import open

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension

# This is needed to build cython extensions.
from setuptools.command.build_ext import build_ext

# Package configuration should all be defined here for easy access.
# Update these values as best fits your particular package.

name = "sample_package"

description = "xBrite Sample Package."

author = "xBrite contributors"

author_email = "xbrite@example.com"

url = "https://github.com/xBrite/sample-python-package"

license = "MIT License"

keywords = "xBrite"

classifiers = [
    # CHANGEME: Update the classifiers as appropriate
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: {}".format(license),
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

setup_requires = (
    # CHANGEME: This module contains special handling for bootstrapping a
    #           project for cython and numpy. However, since these are
    #           specialty packages (especially during setup), we leave them
    #           commented out. Uncomment them here and in the tox section of
    #           pyproject.toml if wish to use them.
    # "cython",
    # "numpy",
)

install_requires = setup_requires + (
    # CHANGEME: Put your package"s requirements here.  A requirements.txt file
    #           is not recommended.
    # "sample_package",
    # "other_sample_package",
)

tests_require = install_requires + (
    "pytest",
    "pytest-runner",
    "tox",
    "flake8",  # linting
    "mypy",  # linting
)

dev_require = tests_require + (
    "pip-tools",  # for managing packages and building requirements.txt
    "black",  # autoformatting
    "ptvsd",  # vscode python debugging
    "isort",  # for auto-sorting imports
    "autoflake",  # for auto-remove unused imports
)

dependency_links = (
    # CHANGEME: Install any private dependency links here.
)

entry_points = {
    # CHANGEME: Set up any appropriate entry points here, e.g. console_scripts
    # "console_scripts": [
    #     "sample_script = sample_package.example_script:main",
    # ],
}

# Setting this to true will make sure any binaries in MANIFEST.in
# get included with the package when it is distributed.
# See: http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
include_package_data = True

################################################
# Please try not to touch things below this line
################################################

HERE = os.path.abspath(os.path.dirname(__file__))
MODULE_PATH = os.path.join(HERE, name.replace("-", "_"))

# Get the long description from the README file
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Load the version by reading the package directly, so we don"t run into
# dependency loops by importing it into setup.py
version = None
with open(os.path.join(MODULE_PATH, "__init__.py")) as init_file:
    for line in init_file:
        print(line)
        m = re.search(r"\b(?:__version__|VERSION)\b\s*(?::\s*\w+\s*)=\s*(.+?)$", line)
        if m:
            version = eval(m.group(1))
            break
assert version is not None, "Couldn't find version string."


class BuildExtWithNumpyWorkaround(build_ext):
    """
    We need `numpy.get_include()` in order to build cython+numpy packages on some
    environments (I"m looking at you, MacOS), but we don"t want setup.py to depend
    on it and cause ImportErrors that would prevent things like pip from determining
    the what packages setup actually requires.

    This also includes a check so that it doesn"t even try to include import numpy
    unless cython ext_modules are actually detected, and `numpy` is included in
    the `setup_requires` list.

    See: https://stackoverflow.com/questions/19919905/how-to-bootstrap-numpy-installation-in-setup-py
    """

    NEED_NUMPY_INCLUDE = False

    def finalize_options(self):
        build_ext.finalize_options(self)  # old-style class can"t call super() properly
        if self.NEED_NUMPY_INCLUDE:
            # Prevent numpy from thinking it"s still in its own setup process:
            __builtins__.__NUMPY_SETUP__ = False
            import numpy

            self.include_dirs.append(numpy.get_include())


def make_ext_modules():
    """
    Walk the module tree looking for cython files and return a list of Extensions() from them.
    See: http://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
    """
    extensions = []
    if "cython" in setup_requires:
        cur_dir = os.getcwd()
        (parent_dir, module_dir) = os.path.split(MODULE_PATH)
        try:
            if parent_dir:
                os.chdir(parent_dir)
            for info in os.walk(module_dir):
                dir_path = info[0]
                # subdirs = info[1]
                pyx_files = [f for f in info[2] if f.endswith(".pyx")]
                pxd_files = [f for f in info[2] if f.endswith(".pxd")]
                for pyx in pyx_files:
                    sources = [os.path.join(dir_path, pyx)]
                    module = pyx[:-4]
                    pxd = module + ".pxd"
                    if pxd in pxd_files:
                        sources.append(os.path.join(dir_path, pxd))
                    if sources:
                        ext_name = ".".join(dir_path.split(os.sep) + [module])
                        extensions.append(Extension(ext_name, sources=sources))
        finally:
            os.chdir(cur_dir)
    if extensions and "numpy" in setup_requires:
        BuildExtWithNumpyWorkaround.NEED_NUMPY_INCLUDE = True
    return extensions


setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    classifiers=classifiers,
    keywords=keywords,
    cmdclass={"build_ext": BuildExtWithNumpyWorkaround},
    setup_requires=setup_requires,
    # Specify the specific modules (if any) that cython should compile
    ext_modules=make_ext_modules(),
    # This package only installs its base module, and a bunch of dependencies
    packages=find_packages(exclude=["bin", "contrib", "docs", "tests"]),
    include_package_data=include_package_data,
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points=entry_points,
    # In order to keep tox *and* setup happy, we need to define the test requirements twice...
    extras_require={
        "test": tests_require,
        "dev": dev_require,
    },
    tests_require=tests_require,
    test_suite="py.test",
)
