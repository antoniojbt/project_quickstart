'''
pipeline_name
=============

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

These are based on CGATPipelines_ and Ruffus_, not docopt.

.. _CGATPipelines: https://github.com/CGATOxford/CGATPipelines

.. _Ruffus: http://www.ruffus.org.uk/


For command line help type:

    python pipeline_pq_example.py --help

Configuration
=============

This pipeline is built using a Ruffus/CGAT approach. You need to have Python,
Ruffus, CGAT core tools and any other specific dependencies needed for this
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
# Get modules needed:
import sys
import os

# Pipeline:
import ruffus

# Database:
import sqlite3

# Try getting CGAT: 
try:
    import CGAT.IOTools as IOTools
    import CGATPipelines.Pipeline as P
    import CGATPipelines.Experiment as E

except ImportError:
    print('\n', "Warning: Couldn't import CGAT modules, these are required. Exiting...")
    raise

# required to make iteritems python2 and python3 compatible
from builtins import dict

# Import this project's module, uncomment if building something more elaborate: 
#try: 
#    import module_template.py 

#except ImportError: 
#    print("Could not import this project's module, exiting") 
#    raise 

# Import additional packages: 

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
# Specific pipeline tasks
@transform((INI_file, "conf.py"),
           regex("(.*)\.(.*)"),
           r"\1.counts")
def countWords(infile, outfile):
    '''count the number of words in the pipeline configuration files.'''

    # the command line statement we want to execute
    statement = '''awk 'BEGIN { printf("word\\tfreq\\n"); }
    {for (i = 1; i <= NF; i++) freq[$i]++}
    END { for (word in freq) printf "%%s\\t%%d\\n", word, freq[word] }'
    < %(infile)s > %(outfile)s'''

    # execute command in variable statement.
    #
    # The command will be sent to the cluster.  The statement will be
    # interpolated with any options that are defined in in the
    # configuration files or variable that are declared in the calling
    # function.  For example, %(infile)s will we substituted with the
    # contents of the variable "infile".
    P.run()


@transform(countWords,
           suffix(".counts"),
           "_counts.load")
def loadWordCounts(infile, outfile):
    '''load results of word counting into database.'''
    P.load(infile, outfile, "--add-index=word")
################

################
# Generic pipeline tasks
@follows(loadWordCounts)
def full():
    pass
################

################
#def build_report():
#    '''build report from scratch.
#
#    Any existing report will be overwritten.
#    '''

#    E.info("starting report build process from scratch")
#    P.run_report(clean=True)
################

################
if __name__ == "__main__":
    sys.exit(P.main(sys.argv))
################
