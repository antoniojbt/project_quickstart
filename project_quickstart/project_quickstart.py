# -*- coding: utf-8 -*-

'''project_quickstart.py - setup a new python based project
===========================================================

:Author: Antonio Berlanga-Taylor
:Release: $Id$
:Date: |today|


Purpose
=======

This script creates a python data science project template. The main idea is
to
be able to easily turn a project into a package with software testing, version
control, reporting, docs, etc. It has:

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

Once you've quickstarted your project you can run script_quickstart.py to
quickly create a Python or R script template.

For a pipeline quickstart based on a Ruffus and CGAT framework see also:
https://github.com/CGATOxford/CGATPipelines/blob/master/scripts/pipeline_quickstart.py
(on which this code is based on)


Usage and Options
=================

Create a new directory, subfolders and files in the current directory that will
help quickstart your data science project with packaging, testing, scripts and
other templates.

.. These are using docopt: http://docopt.org/
.. https://github.com/docopt/docopt
.. An example for loading arguments from an INI file:
.. https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
.. http://docopt.readthedocs.io/en/latest/#help-message-format
.. Basic reminders for docopt:
    Use two spaces to separate options with their informal description
    () are required, [] are optional
    Default values are specified in the Options section with eg [default:
    xxx.log]

.. See also Schema for input argument validation, e.g.:
    https://github.com/docopt/docopt/blob/master/examples/validation_example.py

.. Usage pattern in docopt can't have empty lines and ends with an empty line.
   The first word after usage\: is interpreted as the program's name (e.g.
   'python xxx.py' makes it think your programme is called 'python' with
   option 'xxx.py')
.. docopt reads multi-line descriptions in Options so 80 character lines can be
   wrapped.
.. 'Usage' and 'Options' case insensitive and followed by ':' are recognised by
   docopt in the docstrings.
.. docopt


Usage:
       project_quickstart.py (--project-name=<project_name> | -n <project_name>) ...
       project_quickstart.py [--update | -u]
       project_quickstart.py [--script-python=<script_name>]
       project_quickstart.py [--script-R=<script_name>]
       project_quickstart.py [-f | --force]
       project_quickstart.py [-h | --help]
       project_quickstart.py [--version]
       project_quickstart.py [--quiet]
       project_quickstart.py [--verbose]
       project_quickstart.py [--log=<log_file> | -L <log_file>]


Options:
    --project-name=DIR -n DIR     Starts a new project, 'project_' is prefixed
    --update -u                   Propagate changes made in project_quickstart.ini
    --script-python=FILE          Create a python script template, '.py' is appended
    --script-R=FILE               Create an R script template, '.R' is appended
    -f --force                    Take care, forces to overwrite files and directories.
    -h --help                     Show this screen.
    --version                     Show version.
    --quiet                       Print less text.
    --verbose                     Print more text.
    -L FILE --log=FILE            Log file name. [default: project_quickstart.log]


Documentation
=============

.. todo::

  Add docs
  Add tree structure
  New string formatting https://pyformat.info/ '{} {}'.format('one', 'two')

Code
====
'''

##############################
import sys
import re
import os
import shutil
import collections
import glob
import string

try:
    import configparser
except ImportError:  # Py2 to Py3
    import ConfigParser as configparser

try:
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO

# Modules not in core library:
# import CGAT.Experiment as E
import docopt


# project_quickstart.py modules:
# import quickstart_utilities.py as quickUtils


# Check configuration and print to standard out
# See:
# https://github.com/CGATOxford/CGATPipelines/blob/master/CGATPipelines/
# Pipeline/Parameters.py
# https://github.com/CGATOxford/cgat/blob/master/CGAT/Experiment.py

# Global variable for configuration file ('.ini')
# allow_no_value addition is from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# By using `allow_no_value=True` we are allowed to
# write `--force` instead of `--force=true` below.
CONFIG = configparser.ConfigParser(allow_no_value = True)


'''
class TriggeredDefaultFactory:
    with_default = False

    def __call__(self):
        if TriggeredDefaultFactory.with_default:
            return str()
        else:
            print("Missing argument, see python project_quickstart.py --help")
            raise KeyError("Missing parameter accessed")
'''

# Global variable for parameter interpolation in commands
# This is a dictionary that can be switched between defaultdict
# and normal dict behaviour.
#PARAMS = collections.defaultdict(TriggeredDefaultFactory())

# patch - if --help or -h in command line arguments,
# switch to a default dict to avoid missing paramater
# failures

# TO DO: (see E.py)
# if "--help" in sys.argv or "-h" in sys.argv:
#    TriggeredDefaultFactory.with_default = True

CONFIG.read('project_quickstart.ini')
for key in CONFIG:
    print(key, CONFIG[key])

# docopt requires Nones to be passed as False:
# quickUtils.load_ini_config()
# results = ini_values

##############################


##############################
# To delete:
prog_version = '0.1'

def main(options):
    ''' with docopt main() expects a dictionary with arguments from docopt()
    docopt will automatically check your docstrings for usage, set -h, etc.
    '''
    docopt_error_msg = str('Options in place:' + '\n' +
                           str(docopt.docopt(__doc__)))

    try:
        # Parse arguments, use file docstring as a parameter definition:
        # These are required, exit with message if not present:
        if not options['--project-name']:
            print(''' Error in  the options given, a project name is required, such
                      as "super", which will be appended to "project_" .
                      Try python project_quickstart.py --help .''')
            print(docopt_error_msg)
            sys.exit()
        elif options['--project-name']:
            project_name = str('project_{}').format(options['--project-name'])

        # These arguments are optional:
        if options['--force']:  # overwrite directory
            print('Force overwriting directories and files')
            print('Option not in use at the moment')
            pass  # TO DO
        if not options['--log']:
            log = str('project_quickstart.log')
        else:
            log = '{}'.format(options['--log'])
        if options['--update']:
            print(''' After manually editing the ini file run to
                    propagate changes.''')
            print('Option not in use at the moment')
            pass  # TO DO
        if options['--script-python'] and len(options['--script-python']) > 0:
            print(''' Creating a Python script template. A softlink is
                  created in the current working directory and the
                  actual file in xxx/code/scripts/ ''')
            script_name = str('{}.py').format.options['--script-python']
            print(script_name)
        elif options['--script-python'] and len(options['--script-python']) == 0:
            print(''' You need to provide a script name. This will be prefixed to
                  ".py" ''')
            print(docopt_error_msg)
            sys.exit()
        if options['--script-R'] and len(options['--script-R']) > 0:
            print(''' Creating an R script template. A softlink is
                  created in the current working directory and the
                  actual file in xxx/code/scripts/ ''')
            script_name = str('{}.R').format.options['--script-R']
            print(script_name)
        elif options['--script-R'] and len(options['--script-R']) == 0:
            print(''' You need to provide a script name. This will be prefixed to
                  ".R" ''')
            print(docopt_error_msg)
            sys.exit()

    # Handle exceptions:
    except docopt.DocoptExit:
        print(''' Invalid option or missing argument,
        try project_quickstart.py --help''')
        print(docopt_error_msg)
        raise

    # Set up default paths, directoy and file names:
    project_dir = str(os.getcwd() + '/' + project_name)

    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    # Get locations of source code and of the 'templates'
    # folder to copy over from:
    source_dir = os.path.join(sys.exec_prefix, "/bin")
    template_dir = os.path.join(source_dir, '/project_quickstart/templates/')
    project_template = os.path.join(template_dir, '/project_template')
    manuscript_dir = os.path.join(project_dir, '/manuscript')
    code_dir = os.path.join(project_dir, '/code')
    data_dir = os.path.join(project_dir, '/data')
    script_template_py = str('python_script_template.py')
    script_template_R = str('R_script_template.R')

    print(str('Paths discovered:' + '\n' +
          source_dir + '\n' +
          template_dir + '\n' +
          project_template + '\n' +
          'Creating the structure for {} in:' + '\n' +
          project_dir).format(project_name))

    # Create directories:
    # TO DO: pass these from ini file
    for d in (({1},
              "{1}/code",
              "{1}/data",
              "{1}/data/raw",
              "{1}/data/processed",
              "{1}/data/external",
              "{1}/results_1",
              "{1}/manuscript").format(project_name)):

        tree_dir = os.path.join(project_dir, d)

        if not os.path.exists(tree_dir):
            os.makedirs(tree_dir)

    # Copy files from template directory:
    def projectTemplate(source_dir, project_dir):
        '''
        Copy across project template files and directories for
        a Python/GitHub/etc setup.
        TO DO: 'code' dir is hard coded, change to ini parameter later
        The intention is to use the 'code' dir as a
        GitHub/packageable directory
        '''
        copy_from = project_template
        copy_to = code_dir

        if os.path.exists(copy_to) and not options['--force']:
            raise OSError('''
                          file {} already exists - not overwriting,
                          see --help or use --force
                          to overwrite.
                          '''.format(script_name)
                          )
        else:
            shutil.copytree(copy_from, copy_to)
            # https://docs.python.org/3/library/shutil.html

    # Replace all instances of template with 'name' from project_'name' as
    # specified in options:
    def rename(project_dir, old_substring, project_name):
        '''
        rename 'template' to 'project' from template file names
        '''
        for dirpath, dirname, filename in os.walk(project_dir):
            for filename in files:
                os.rename(os.path.join(project_dir, filename),
                          os.path.join(project_dir, filename.replace(
                              'template', {})).format(project_name)
                          )

    def manuscriptTemplates(template_dir, manuscript_dir):
        '''
        Copy the manuscript and lab_notebook templates
        to the 'manuscript' directory.
        '''

        files = glob.glob('(*).rst')
        for f in files:
            shutil.copy(template_dir, manuscript_dir)

    def scriptTemplate(python_script, R_script):
        ''' Copy script templates and rename
        them according to option given
        '''
        copy_to = os.path.join(code_dir, '/scripts')

        if option['--script-python']:
            if os.path.exists(copy_to) and not options['--force']:
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_py)
                shutil.copy(copy_from, copy_to)
                os.rename(os.path.join(copy_to, script_template_py),
                          filename.replace('template', {})).format(script_name)

        elif option['--script-R']:
            if os.path.exists(copy_to) and not options['--force']:
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_R)
                shutil.copy(copy_from, copy_to)
                os.rename(os.path.join(copy_to, script_template_R),
                          filename.replace('template',
                                           {})).format(script_name)

        else:
            raise ValueError(''' Bad arguments/options used for script template,
            try --help''')

    # Print a nice welcome message (if successful):
    print(""" Done, welcome to your {1}!

    The folder structure and files have been successfully copied to {2}.
    Files have been copied 'as is'. You can edit the configuration file
    ('xxx.ini') and run:

    python project quickstart.py --update

    to update files with your chosen parameters (note files get
    overwritten though).

    The folder structure is {3}.

    Remember to back up code, data and manuscript directories
    (or your equivalent). The {4} (or equivalent) directory can be
    uploaded to a version control system for example
    (file templates are for GitHub). Link to Travis CI, Zenodo and
    ReadtheDocs (notes and reminders within the files copied over)
    if needed. Script templates are in the {4}/scripts/ location
    (or equivalent if renamed). You can put scripts and modules
    in the {4}/code/scripts/ location and pipelines (eg Ruffus/CGAT or others)
    in the {4}/code/{1} location for example.
    Sphinx can be used to render your rst documents in the {5} directory.
    Basic, single rst template files have been generated already.
    Use sphinxqhickstart if you want a fuller version for instance.

    Feel free to raise issues, fork or contribute at:

    https://github.com/AntonioJBT/project_quickstart

    Have fun!
    """.format(project_name,
               project_dir,
               tree_dir,
               code_dir,
               manuscript_dir,
               data_dir)
          )

if __name__ == '__main__':
    # if using docopt:
    # it will check all arguments pass, if not exits with 'Usage:':
    options = docopt.docopt(__doc__, version='{}'.format(prog_version))
         # switch to template from INI with t = string.Template('$version') ;
         # t.substitute({'version':0.1})
    # if arguments are valid, run the program:
    sys.exit(main(options))
