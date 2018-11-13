'''
pytest_helper_funcs.py
=======================

:Author: |author_names|
:Release: |version|
:Date: |today|


Purpose
=======

Helper functions for tests for project_quickstart

Import as a module

'''
##############
# Get all the modules needed
# System:
import os
import hashlib
import subprocess
import sys
##############


##############
# Helper functions
# Run each project_quickstart CLI option:
def run_CLI_options(options):
    '''
    Execute each command-line option. Pass options as a list of strings,
    each being a command with arguments for the CLI package to test.
    If the process fails it is communicated (check = True with output captured).
    '''

    for option in options:
        print(option)
        subprocess.run(option, capture_output = True, check = True)

    return


# Get trees for each directory:
def create_dir_tree(dirs, suffix):
    '''
    For each directory created during tests create a tree directory using
    ls -Ra1
    Provide one or more directories as a list and a suffix for the output trees.
    '''
    for d in dirs:
        print(d)
        name = str(d + suffix)
        subprocess.run(['ls', '-Ra1', d,
                        '>',
                        name,
                        ],
                       capture_output = True
                       )

    return


# Collect files with tree directories:
def collect_files(dir_to_search, suffix):
    '''
    Collect files to compare from a named directory and ending with a given suffix
    '''
    # Collect files:
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(dir_to_search):
        for f in filenames:
            if f.endswith(suffix):
                print(f)
                file_list.extend(f)
        break

    return(file_list)


# Function to compare text files:
def compare_files(ref, test):
    '''
    Compare text files line by line. Only provides a coarse output.
    '''
    # Read each file:
    with open(ref, 'r'):
        ref = ref.read()

    with open(test, 'r'):
        test = test.read()

    if ref != test:
        sys.exit('''Files are not the same, comparing:
                 {}
                 and
                 {}'''.format(ref, test)
                 )
    return


# Compare two sets of text files:
def compare_all_files(test_list, ref_list):
    '''
    Compare files between test_list and ref_list
    '''

    # Sort files:
    ref_list = ref_list.sort()
    test_list = test_list.sort()

    for ref in ref_list:
        for test in test_list:
            if ref == test:
                compare_files(ref, test)
            break  # and continue to the next set of matching filenames

    return


# Compute md5sums for each file created from each CLI option run:
def compute_checksum(filename):
    '''
    Return md5 checksum
    '''
    md5 = hashlib.md5(open(filename, 'rb').read()).hexdigest()

    return(md5)
##############
