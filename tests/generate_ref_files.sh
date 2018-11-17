#!/usr/bin/env bash

###########################
# Generate reference files to test against for project_quickstart:
# These should be the same as options in test_project_quickstart.py
# After updating templates, commit and push, travis will fail, locally run:
# pip install git+git://github.com/AntonioJBT/project_quickstart.git
# and run this file to generate the new reference set.
###########################

###########################
# Set bash script options

# exit when a command fails:
set -o errexit

# exit if any pipe commands fail:
set -o pipefail

# exit if there are undeclared variables:
set -o nounset

# trace what gets executed:
# set -o xtrace
set -o errtrace
###########################

###########################
# Create folder, this should be the same as in test file: 
ref_dir='ref_files'
###########################

###########################
mkdir ${ref_dir}
cd ${ref_dir}

# test_name should also be the same as in the test file:
test_name='pq_test_ref'

# Test command line options that only go to stdout:
project_quickstart --version
project_quickstart -h
project_quickstart --help

# Test options that generate files and use these as references:
project_quickstart -n ${test_name}
project_quickstart --script-python=${test_name}
project_quickstart --script-R=${test_name}
project_quickstart --script-pipeline=${test_name}
project_quickstart --example

# Generate files with tree directories:
# OS X ls doesn't seem to print out first grouping folder, Ubuntu does, which then causes travis to fail
# Use python file lists only instead
# This (inside this script) does not give folder grouping and errors on travis but not locally:
# Run these manually:
# echo 'Run ls commands manually to provide folder grouping...'
# echo 'ls -Ra1 '${ref_dir}'/pq_test_ref > '${ref_dir}'/pq_test_ref.tree'
# echo 'ls -Ra1 '${ref_dir}'/pq_example > '${ref_dir}'/pq_example.tree'
# echo 'ls -Ra1 '${ref_dir}'/pipeline_pq_test_ref > '${ref_dir}'/pipeline_pq_test_ref.tree'
###########################

###########################
# Generate lists of files from directories using python (ls -Ra1 has different flavours?):
python ../generate_python_file_lists.py
###########################
