#!/usr/bin/env bash

# Set bash script options:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
set -o errexit
set -o pipefail
set -o nounset


# Variables to substitute:
greeting=hello
name=antonio
more_to_say=$1

# If running from the command line and using positional arguments:
#greeting=$1
#name=$2

# Run command:
echo ${greeting} ${name} ${1}
