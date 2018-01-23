#!/usr/bin/env bash

###########################
# Some references to check:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
# http://jvns.ca/blog/2017/03/26/bash-quirks/
# Bash traps:
# http://aplawrence.com/Basics/trapping_errors.html
# https://stelfox.net/blog/2013/11/fail-fast-in-bash-scripts/
###########################

###########################
# Set bash script options

# exit when a command fails
set -o errexit

# exit if any pipe commands fail
set -o pipefail

# exit when your script tries to use undeclared variables
set -o nounset

# trace what gets executed
set -o xtrace

set -o errtrace
###########################

###########################
# Variables to substitute:
greeting=hello
name=antonio
more_to_say=$1
###########################

###########################
# If running from the command line and using positional arguments:
#greeting=$1
#name=$2

# Run command:
echo ${greeting} ${name} ${1}
###########################
