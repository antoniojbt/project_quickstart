'''
template.py
===========

:Author: |author_names|
:Release: |version|
:Date: |today|


Purpose
=======

|description|

This is a template for a python script. It is runnable though and gives some
output to screen.

Usage and options
=================

These are based on docopt_, see examples_.

.. _docopt: https://github.com/docopt/docopt

.. _examples: https://github.com/docopt/docopt/blob/master/examples/options_example.py


Usage:
       template.py (--a_number=<int>) [-I FILE] [-O FILE]
       template.py [-h | --help] [-V | --version] [-f --force] [-L | --log]

Options:
    --a_number=<int>    Give a number just for fun
    -I FILE             Input file name
    -O FILE             Output file name
    -h --help           Show this screen
    -V --version        Show version
    -f --force          Force overwrite
    -L --log            Log file name


Input:

None

Output:

Prints a few things to screen


Requirements:

Python packages only

Documentation
=============

    For more information see:

        |url|

'''
##############
# Get all the modules needed
# System:
import os
import sys
import glob

# Options and help:
import docopt

# Data science:
import pandas as pd
import numpy as np

# required to make iteritems python2 and python3 compatible
from builtins import dict

# Try getting CGAT:
try:
    import CGAT.IOTools as IOTools
    import CGATPipeline.Pipeline as P
    import CGATPipeline.Experiment as E

except ImportError:
    print("Warning: Couldn't import CGAT modules, continuing without")
    pass
##############

##############
#####
# Some basic Python reminders
# Slicing/indexing excludes the last number
# Lists are 0 based
# PEP8 has 80 character limit and 4 spaces for indentation, do not use tabs, much less mix
# Python operator precedence: https://www.tutorialspoint.com/python/operators_precedence_example.htm
# dictionaries are accessed as my_dict[2] ; '2' == key, not index ; while my_list[2] is an index ; use assert if ambigous
# modulo is % (the remainder) ; // gives the integer of the division
# lists and dictionaries are mutable; tuples immutable
# Functional programming
# OOP
# regex
#####

#####
# Basic function structure:
def my_func(a_number):
    '''
    Comment the function, this will be pulled automatically into the documentation.
    '''

    # Make sure the setup is correct for this function:
    assert True == True
    print('Do something with "a_number"')
    x = a_number
    OK = x * a_number
    return(OK)
#####

#####
def handleErrors():
    ''' A function to handle errors '''
    try:
        print('Pass something')
    except TypeError: #some error to catch
        print('Wrong type of variable') #some helpful message or other option
        raise # Raise the system error anyway
    except: # 'except:' by itself will catch everything, potentially disastrous
        print("Unexpected error:", sys.exc_info()[0])
        raise # even if caught raise the error
    finally:
        print('Did this work?')#do this regardless of the above, also dangerous
#####

#####
def elseIf(a_number):
    ''' A simple function with an if else structure'''
    x = a_number
    if x > 1:
        print('Your number is positive')
    elif x < 1:
        print('Your number is negative')
    else:
        print('You gave a zero')
#####

#####
# Basic OOP class structure:
# Form e.g.: https://www.tutorialspoint.com/python/python_classes_objects.htm
class SuperHero:
    '''
    Common base class for all employees
    '''
    SuperSaves = 0

    def __init__(self, name, power, saves):
       self.name = name
       self.power = power
       self.saves = saves
       SuperHero.SuperSaves += saves

    def displaySaves(self):
      print("Total SuperHero saves %d" % SuperHero.SuperSaves)

    def displaySuperHero(self):
        print("Name: ", self.name,  " Power: ", self.power, " Saves: ", self.saves)

def runOOPHeroes(saves):
    ''' Example function that runs OOP code for SuperHeroes '''
    # First object in class:
    super1 = SuperHero("SuperWoman", 'Strong', saves)
    # Second object in class:
    super2 = SuperHero("AveJoe", 'Common Sense', saves = (saves - 2))

    # Check the Attributes:
    super1.displaySuperHero()
    super2.displaySuperHero()
    print("Total SuperHero saves %d" % SuperHero.SuperSaves)
    return()
#####

def main():
    ''' with docopt main() expects a dictionary with arguments from docopt()
    docopt will automatically check your docstrings for usage, set -h, etc.
    '''
    version = 'my "first version" (aka something like "0.1.1")'
    options = docopt.docopt(__doc__, version = version)
    welcome_msg = str('\n' + 'Welcome to template.py. This is {}' +
            '\n').format(version)
    print(welcome_msg)
    docopt_error_msg = str('template.py exited due to an error.' + '\n')
    docopt_error_msg = str(docopt_error_msg
                           + '\n'
                           + 'Try template.py --help'
                           + '\n' + '\n'
                           + 'Options in place:'
                           + '\n'
                           + str(options)
                           + '\n'
                           )

    try:
        if options['--a_number'] and len(options['--a_number']) > 0:
            a_number = str(options['--a_number']).strip('[]').strip("''")
            a_number = int(a_number)
            print('Your chosen number for SuperHeroes is: {}'.format(a_number))
            print(''' This number will also be used for the elseIf function
                      example. ''')
            # Call all the functions described above here:
            my_func(a_number)
            elseIf(a_number = a_number)
            handleErrors()
            runOOPHeroes(saves = a_number)
            print('Ran the tests above and finished succesfully. That s all')

        else:
            print(docopt_error_msg)
            print(''' You need to provide a number for a_number. Exiting...''')
            sys.exit()

    # Handle exceptions:
    except docopt.DocoptExit:
        print(docopt_error_msg)
        raise
##############


##############
# Finish and exit with docopt arguments:
if __name__ == '__main__':
    sys.exit(main())
##############
