#!/usr/bin/env bash

###########################
# Some references to check:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
# http://jvns.ca/blog/2017/03/26/bash-quirks/
# Bash traps:
# http://aplawrence.com/Basics/trapping_errors.html
# https://stelfox.net/blog/2013/11/fail-fast-in-bash-scripts/

# TO DO:
# In future check:
# https://github.com/ralish/bash-script-template
# https://natelandau.com/boilerplate-shell-script-template/
# https://unix.stackexchange.com/questions/122845/using-a-b-for-variable-assignment-in-scripts/122848#122848
# https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
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
# Set default values:
# https://stackoverflow.com/questions/9332802/how-to-write-a-bash-script-that-takes-optional-input-arguments
param_default=${1-use_foo_if_not_set}
###########################

###########################
# If running from the command line and using positional arguments:
#greeting=$1
#name=$2

# Run command:
echo ${greeting} ${name} ${1}
###########################
