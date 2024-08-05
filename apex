#!/bin/bash
# This script is a wrapper for running the Python CLI

# Resolve the directory of the current script, following any symlinks
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
BASEDIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"

# Execute the Python script with all passed arguments
python3 "$BASEDIR/cli/apex.py" "$@"
