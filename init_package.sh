#!/bin/bash

set -e

DEFAULT_PYTHON_VERSION="3.7.8"

# Request and confirm the new package name.
while [[ -z $PACKAGE_NAME ]]; do
    echo "What python version should be added to .envrc for local development"
    echo -n "of this package? [$DEFAULT_PYTHON_VERSION] "
    read PYTHON_VERSION
    if [[ ! -z $PYTHON_VERSION ]]; then
        PYTHON_VERSION="$DEFAULT_PYTHON_VERSION"
    fi
    echo "Press ^C to cancel."
    echo "Press ENTER to confirm python version '$PYTHON_VERSION'."
    read

    echo -n "What is the name of this package? "
    read PACKAGE_NAME
    if [[ ! -z $PACKAGE_NAME ]]; then
        echo "Press ^C to cancel."
        echo "Press ENTER to confirm and initialize this package named '$PACKAGE_NAME'."
        read
    fi
done

# Make sure we're in the right directory before we touch anything
PROJECT_ROOT="$(cd "$(dirname "$0")/"; pwd)"
cd $PROJECT_ROOT

# Update envrc with the requested python version
/usr/bin/sed  -e "s,^\(  *use pyenv\) [0-9][0-9.]*,\1 $PYTHON_VERSION," .envrc

# Rename the main package directory
mv sample_package "$PACKAGE_NAME"

# Search through all of the other files in this directory and find/replace to update the name
THIS_FILE=$(basename "$0")
find . -maxdepth 1 -type f -not -name "$THIS_FILE" -exec /usr/bin/sed -i '' -e "s,sample_package,$PACKAGE_NAME,g" {} \+

# Make sure the user knows we're about to remove this script now.
echo "Press ENTER to finish cleaning up and remove this initialization script."
read

/bin/rm -f "$0"

# Add a reminder
echo "Don't forget to read all of the instructions in README.md."
