'''
pipeline_pq_example.py
======================

:Author: |author_name|
:Release: |version|
:Date: |today|


Overview
========

|long_description|


Purpose
=======

.. briefly describe the main purpose and methods of the pipeline


Usage and options
=================

These are based on CGATPipelines_ and Ruffus_

.. _CGATPipelines: https://github.com/CGATOxford/CGATPipelines

.. _Ruffus: http://www.ruffus.org.uk/


For command line help type:

    python pipeline_pq_example.py --help

Configuration
=============

This pipeline is built using a Ruffus/CGAT approach. You need to have Python,
Ruffus, CGAT core tools and any other specific dependencies needed fo this
script.

A configuration file was created at the same time as this script.

Use this to extract any arbitrary parameters that could be changed in future
re-runs of the pipeline.


Input files
===========

.. Describe the input files needed, urls for reference and preferably place
example data somewhere.


Pipeline output
===============

.. Describe output files and results


Requirements
============

CGATPipelines core setup, Ruffus as well as the following
software to be in the path:

.. Add any additional external requirements such as 3rd party software
   or R modules below:

Requirements:

* R >= 1.1
* Python >= 3.5


Documentation
=============

    For more information see:

        |url|

'''
################
from ruffus import *

import sys
import os
import sqlite3

# Check CGAT_core and how to import here:
import CGAT.Experiment as E
import CGATPipelines.Pipeline as P
################

################
# Get pipeline.ini file:
def getINI():
    path = os.path.splitext(__file__)[0]
    paths = [path, os.path.join(os.getcwd(), '..'), os.getcwd()]
    f_count = 0
    for path in paths:
        if os.path.exists(path):
            for f in os.listdir(path):
                if (f.endswith('.ini') and f.startswith('pipeline')):
                    f_count += 1
                    INI_file = f

    if f_count != 1:
        raise ValueError('''No pipeline ini file found or more than one in the
                            directories:
                            {}
                        '''.format(paths)
                        )
    return(INI_file)

# Load options from the config file
INI_file = getINI()
PARAMS = P.getParameters([INI_file])
################

################
# Utility functions
def connect():
    '''utility function to connect to database.

    Use this method to connect to the pipeline database.
    Additional databases can be attached here as well.

    Returns an sqlite3 database handle.
    '''

    dbh = sqlite3.connect(PARAMS["database_name"])
    statement = '''ATTACH DATABASE '%s' as annotations''' % (
        PARAMS["annotations_database"])
    cc = dbh.cursor()
    cc.execute(statement)
    cc.close()

    return dbh
################

################
path_to_scripts = '/Users/antoniob/Documents/github.dir/AntonioJBT/project_quickstart/templates/examples/'

# Specific pipeline tasks

#@transform(countWords,
#           suffix(".counts"),
#           "_counts.load")
#def loadWordCounts(infile, outfile):
#    '''load results of word counting into database.'''
#    P.load(infile, outfile, "--add-index=word")

@mkdir('pq_results')
@originate('pandas_DF')
def createDF():
    '''
    Call a python example script from project_quickstart which creates a pandas dataframe
    '''
    statement = '''
                cd pq_results ;
                python pq_example.py --createDF -O %(outfile)s.tsv
                '''
    P.run()

def run_pq_examples():
    ''' Runs python and R scripts from project_quickstart as examples of a
        pipeline with Ruffus and CGAT tools.
        A dataframe, several plots and a multi-panel plot are generated.
    '''
    # command line statement to execute, to run in bash:
    statement = '''
                Rscript pq_example.R -I %(outfile)s.tsv ;
                checkpoint ;
                Rscript plot_pq_example_pandas.R -I %(outfile)s ;
                checkpoint ;
                python svgutils_pq_example.py \
                        --plotA=pandas_DF_gender_glucose_boxplot.svg \
                        --plotB=pandas_DF_age_histogram.svg ;
                checkpoint ;
                '''

    # execute command in variable statement.
    # The command will be sent to the cluster (by default, but this can be
    # turned off with --local).  The statement will be
    # interpolated with any options that are defined in in the
    # configuration files or variable that are declared in the calling
    # function.  For example, %(infile)s will we substituted with the
    # contents of the variable "infile".
    P.run()


def run_mtcars():
    '''
    A second set of examples from project_quickstart
    Some plots and an html table of a linear regression are generated.
    '''
    # Plots simple examples:
    statement = '''python plot_pq_example.py '''

    # Scripts for mt_cars in R:
    statement = ''' Rscript pq_example_mtcars.R ;
                    checkpoint ;
                    Rscript plot_pq_example_mtcars.R
                    checkpoint ;
                '''
    P.run()

#def build_report():
#    '''build report from scratch.
#
#    Any existing report will be overwritten.
#    '''

#    E.info("starting report build process from scratch")
#    P.run_report(clean=True)

# TO DO:
# docopt and sysargv will conflict between script and Pipeline...
# Finish and exit with docopt arguments:
#if __name__ == '__main__':
#    arguments = docopt(__doc__, version='xxx 0.1')
#    print(arguments)
#    sys.exit(main())

if __name__ == "__main__":
    sys.exit(P.main(sys.argv))
