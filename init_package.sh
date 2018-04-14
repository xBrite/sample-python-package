#!/bin/bash

set -e

# Request and confirm the new package name.
while [[ -z $PACKAGE_NAME ]]; do
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

# Rename the main package directory
mv sample_package "$PACKAGE_NAME"

# Search through all of the other files in this directory and find/replace to update the name
THIS_FILE=$(basename "$0")
find . -maxdepth 1 -type f -not -name "$THIS_FILE" -exec sed -i '' -e "s,sample_package,$PACKAGE_NAME,g" {} \+

# Make sure the user knows we're about to remove this script now.
echo "Press ENTER to finish cleaning up and remove this initialization script."
read

/bin/rm -f "$0"

# Add a reminder
echo "Don't forget to read all of the instructions in README.md."
