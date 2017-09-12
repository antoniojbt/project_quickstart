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
       template.py [--a_number=<int>] [-I FILE] [-O FILE]
       template.py [--createDF] [--sample-size=<int>] [-I FILE] [-O FILE]
       template.py [-h | --help] [-V | --version] [-f --force] [-L | --log]

Options:
    --a_number=<int>    Give a number just for fun
    --createDF          Create a pandas data frame
    --sample-size=<int> Specify a sample size (number of rows) for the dataframe[default: 1000]
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
import pandas
#import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats

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

# Import this project's module, uncomment if building something more elaborate:
#try:
#    import module_template.py

#except ImportError:
#    print("Could not import this project's module, exiting")
#    raise

# Import additional packages:
import string # this is used in the pandas function
import random
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
# If this becomes a more complex project you could move all functions (except
# e.g. main()) to a module.py script.

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

#####
# Create a pandas dataframe, run basic stats, lm, table and plots and save to
# disk:
# See pandas in 10 minutes:
# http://pandas.pydata.org/pandas-docs/stable/10min.html

def id_generator(size = 6,
                 chars = string.ascii_uppercase + string.digits,
                 sample_size = 1000):
    ''' Generates a random sequence of letters and numbers
        Modified from:
        https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python?rq=1
    '''
    ID_list = []
    sample_size = sample_size + 1 # Python index is 0-based, stop number is
                                  # excluded
    for i in range(1, sample_size):
        i = ''.join(random.choice(chars) for i in range(size))
        ID_list.append(i)

    ID_list = pandas.Series(ID_list)
    #print(ID_list.head(),
    #      ID_list.tail(),
    #      ID_list.describe(),
    #      )

    return(ID_list)

def number_generator(lower_bound = 0,
                     upper_bound = 1001,
                     mean = 1,
                     sd = 1,
                     sample_size = 1000):
    ''' Generate a set of random values based on a given mean, standard
        deviation, list size and range from a normal distribution.
        Remember that in Python indexing is 0-based (includes the start
        but excludes the stop).
    '''
    # See:
    # https://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.stats.truncnorm.html
    # stackoverflow how-to-specify-upper-and-lower-limits
    sample = stats.truncnorm.rvs(a = lower_bound,
                                 b = upper_bound,
                                 loc = mean,
                                 scale = sd,
                                 size = sample_size)
    sample = pandas.Series(sample)
    #print(sample.head(),
    #      sample.tail(),
    #      sample.describe(),
    #      )

    return(sample)

def bool_generator(size = 1000):
    ''' Generate a list of random values given a size for booleans
        (e.g. male or female)
    '''
    gender = []
    size = size + 1
    for n in range(1, size):
        n = random.choice(['male', 'female'])
        gender.append(n)

    gender = pandas.Series(gender)
    #print(gender.head(),
    #      gender.tail(),
    #      gender.describe(),
    #      )
    return(gender)

def createDF(sample_size = 1000):
    ''' Generate a pandas dataframe that uses random IDs and random values from
        given distributions of four variables.
    '''
    # "Generate a pandas dataframe by passing a dict of objects that can be
    # converted to series-like."
    # These are just numbers, nothing is adjusted, weighted, etc., the means
    # and SDs are arbitrary. Some values though:
    # age: 40.0 average age of the UK population
    # gender: 50.89% in 2011 apparently
    # glucose: Normal – Fasting plasma glucose <100 mg/dL (5.6 mmol/L)
    # BMI: roughly 26 in men and women for the UK in 2010
    # Some references:
    # https://en.wikipedia.org/wiki/Demography_of_the_United_Kingdom
    # https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/overviewoftheukpopulation/july2017
    # https://www.uptodate.com/contents/screening-for-type-2-diabetes-mellitus?source=search_result&search=glucose&selectedTitle=1~150#H7
    # http://www.thelancet.com/cms/attachment/2094506084/2077189969/mmc1.pdf
    # https://www.uptodate.com/contents/image?imageKey=ENDO%2F73797&topicKey=ENDO%2F1798&rank=1~150&source=see_link&search=hypoglycemia

    print('Sample size is: ', sample_size)
    random_df = pandas.DataFrame({'ID': id_generator(size = 6,
                                                     chars = string.ascii_uppercase + string.digits,
                                                     sample_size = sample_size),
                                  'age': number_generator(lower_bound = 0,
                                                          upper_bound = 121,
                                                          mean = 40.0,
                                                          sd = 20,
                                                          sample_size = sample_size),
                                  'gender': bool_generator(size = 1000),
                                  'glucose': number_generator(lower_bound = 0,
                                                              upper_bound = 501,
                                                              mean = 80,
                                                              sd = 10,
                                                              sample_size = sample_size),
                                  'BMI': number_generator(lower_bound = 0,
                                                          upper_bound = 205,
                                                          mean = 26,
                                                          sd = 3,
                                                          sample_size = sample_size),
                                 })
    print(random_df.head(),
          '\n',
          random_df.tail(),
          '\n',
          random_df.describe(),
          )
    return(random_df)
#####
##############

##############
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
            print("Ran some tests above and finished succesfully. That's all.")

        if (options['--createDF'] and
            options['--sample-size'] and
            len(options['--sample-size']) > 0):

            sample_size = str(options['--sample-size']).strip('[]').strip("''")
            sample_size = int(sample_size)
            print('Your sample size for the pandas dataframe is: {}'.format(sample_size))
            createDF(sample_size = sample_size)

        elif options['--createDF'] and not options['--sample-size']:
            print(''' Using default values for sample size to create a pandas
                      dataframe.''')
            createDF()

        else:
            print(docopt_error_msg)
            print(''' Did you provide a number for --a_number?
                      Did you ask for the --createDF option?
                      Is your --sample-size an integer and greater than 0?
                      Exiting...
                  ''')
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
