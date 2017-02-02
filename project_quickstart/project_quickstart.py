'''project_quickstart.py - setup a new python based project
===========================================================

:Author: Antonio Berlanga-Taylor
:Release: $Id$
:Date: |today|

Purpose
-------

This script creates a python data science project template. The main idea is to be able to easily turn 
a project into a package with software testing, version control, reporting, docs, etc. It has:

    Reproducibility concepts in mind
    Ruffus as a pipeline tool and CGAT tools for support
    Python programming and packaging
    restructuredText and Sphinx for reporting
    Travis and tox for testing
    Conda and Docker for management and development
    GitHub for version control

I've additionally put some basic instructions/reminders to link GitHub with:

    ReadtheDocs
    Zenodo (for archiving your code and generating a DOI)
    Travis CI.

Once you've quickstarted your project you can run script_quickstart.py to quickly
create a Python or R script template. 

For a pipeline quickstart based on a Ruffus and CGAT framework see also:
https://github.com/CGATOxford/CGATPipelines/blob/master/scripts/pipeline_quickstart.py
(on which this code is based on)

Usage and Options
=================
Quickstart a data science project with a folder structure and script, packaging, testing, etc. templates

.. These are using docopt: http://docopt.org/
.. https://github.com/docopt/docopt
.. An example for loading arguments from an INI file: https://github.com/docopt/docopt/blob/master/examples/config_file_example.py

Usage:
    project_quickstart.py (--project_name=<project_name>) ...

to start a new project ('project_' will be prefixed)
This will create a new directory, subfolders and files in the current directory that will help quickstart your data science project.

    project_quickstart.py (--project_name | -n) <project_name> 
    project_quickstart.py --update | -u 
    project_quickstart.py -f | --force
    project_quickstart.py -h | --help
    project_quickstart.py --version
    project_quickstart.py --quiet
    project_quickstart.py --verbose
    project_quickstart.py [-L | --log] <project_quickstart.log>
    
Options:
    --update -u  Configure the project_quickstart.ini manually and run this option to propagate changes.
    -f --force   Take care, forces to overwrite files and directories.
    -h --help    Show this screen.
    --version    Show version.
    --quiet      Print less text.
    --verbose    Print more text.
    -L --log     Log file name. [default: project_quickstart.log]

Documentation
-------------

.. todo::

  Add docs
  Add tree structure
  New string formatting https://pyformat.info/ '{} {}'.format('one', 'two')

Code
----
'''

##############################
import sys
import re
import os
import shutil
import collections
#import CGAT.Experiment as E
from docopt import docopt

try:
    import configparser
except ImportError: # Py2 to Py3
    import ConfigParser as configparser

# Check configuration and print to standard out
# See https://github.com/CGATOxford/CGATPipelines/blob/master/CGATPipelines/Pipeline/Parameters.py
# https://github.com/CGATOxford/cgat/blob/master/CGAT/Experiment.py

# Global variable for configuration file ('.ini'):
CONFIG = configparser.ConfigParser()

class TriggeredDefaultFactory:
    with_default = False

    def __call__(self):
        if TriggeredDefaultFactory.with_default:
            return str()
        else:
            raise KeyError("missing parameter accessed")

# Global variable for parameter interpolation in commands
# This is a dictionary that can be switched between defaultdict
# and normal dict behaviour.
PARAMS = collections.defaultdict(TriggeredDefaultFactory())

# patch - if --help or -h in command line arguments,
# switch to a default dict to avoid missing paramater
# failures

# TO DO: (see E.py)
#if "--help" in sys.argv or "-h" in sys.argv:
#    TriggeredDefaultFactory.with_default = True

CONFIG.read('project_quickstart.ini')
for key in CONFIG:
    print key, CONFIG[key]
##############################

    
##############################
def main():
    # Set up arguments (see docopt above):
    try:
        # Parse arguments, use file docstring as a parameter definition:
        arguments = docopt(__doc__, version = {}).format(prog_version)
        if not options['--project_name']:
            print('Project name required, it will be appended to "project_"')
        if options['--force']: # overwrite directory
            print('Option not in use at the moment')
            pass # TO DO            
        if not options['--log']:
            log = str('project_quickstart.log')
        if options['--update']:
            print('Option not in use at the moment')
            pass # TO DO

    print(arguments)

    # Handle exceptions:
    except docopt.DocoptExit:
        print ('Invalid option, try project_quickstart.py --help')
        raise

    # Set up default paths and directory:
    project_name = {}.format.options['--project_name']
    project_dir = str(os.getcwd() + '/' + project_name)

    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    # Get locations of source code and of the 'templates' folder to copy over from:
    source_dir = os.path.join(sys.exec_prefix, "/bin")
    template_dir = os.path.join(source_dir, '/project_quickstart/templates/')
    project_template = os.path.join(template_dir, '/project_template')
    print('Paths discovered:', '\n', 
          source_dir, '\n', 
          template_dir, '\n', 
          project_template, '\n',
         'Creating the structure for {} in:', '\n',
         project_dir).format(project_name)
    
    # Create directories:
    for d in ("", 
              "code", 
              "data",
              "data/raw",
              "data/processed",
              "data/external",
              "results_1",
              "manuscript"):
    
    tree_dir = os.path.join(project_dir, d)
    if not os.path.exists(tree_dir):
        os.makedirs(tree_dir)

    # Copy files from template directory:
    def copyTemplate(source_dir, project_dir):
        '''
        Copy across template files and directories for a Python/GitHub/etc setup.
        TO DO: 'code' dir is hard coded, change to ini parameter later
        The intention is to use the 'code' dir as a GitHub/packageable directory
        '''
        copy_from = project_template
        copy_to = os.path.join(project_dir, '/code')
        
        if os.path.exists(copy_to) and not options['--force']:
            raise OSError(
                '''file {} already exists - not overwriting, see --help or use --force 
                to overwrite.'''.format(project_name)

        shutil.copytree(copy_from, copyt_to) # https://docs.python.org/3/library/shutil.html


    # Replace all instances of template with 'name' from project_'name' as
    # specified in options:
    def rename(project_dir, old_substring, project_name):
        ''' rename 'template' to 'project' from template file names '''
        for dirpath, dirname, filename in os.walk(project_dir):
            for filename in files:
                os.rename(os.path.join(project_dir, filename), 
                          os.path.join(project_dir, filename.replace('template', {})).format(project_name)

    # Create links for the manuscript and lab_notebook 
    # templates to go into the 'manuscript' directory:
    for template_dir, dest in (("conf.py", "conf.py"),
                      ("pipeline.ini", "pipeline.ini")):
        d = os.path.join("report", dest)
        if os.path.exists(d) and options.force:
            os.unlink(d)
        os.symlink(os.path.join(confdir, src), d)

    # Print a nice welcome message (if successful):
    print(""" Done, welcome to your {}!
    
    The folder structure and files have been successfully copied to {}. 
    Files have been copied 'as is'. You can edit the configuration file and run:
    
    python project quickstart.py --update
    
    to update files with your chosen parameters (note files get overwritten).
    
    The folder structure is {}.
    Feel free to raise issues, fork or contribute at:
    
    https://github.com/AntonioJBT/project_quickstart
    
    Have fun!
    """.format(project_name, project_dir, tree_dir)
         )

if __name__ == '__main__':
    main()
#    sys.exit(main())
