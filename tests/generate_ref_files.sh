#!/usr/bin/env bash

# Generate reference files to test against for project_quickstart:
# These should be the same as options in test_project_quickstart.py
# After updating templates, commit and push, travis will fail, locally run:
# pip install git+git://github.com/AntonioJBT/project_quickstart.git
# and run this file to generate the new reference set.

# Create folder, this should be the same as in test file: 
ref_dir='ref_files'

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
ls -Ra1 pq_test_ref > pq_test_ref.tree
ls -Ra1 pq_example > pq_example.tree
ls -Ra1 pipeline_pq_test_ref > pipeline_pq_test_ref.tree
