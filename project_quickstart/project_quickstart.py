'''
project_quickstart - setup a new python based project
=====================================================

:Author: Antonio Berlanga-Taylor
:Release: |date|
:Date: |today|


Purpose
=======

This script creates a python data science project template. The main idea is
to be able to easily turn a project into a package with software testing, version
control, reporting, docs, etc.

Once you've quickstarted your project you can run run the --script options to
create python and R script templates.

You will need to install other software (e.g. R, Ruffus, Sphinx, etc.) to make
full use depending on your preferences.


Usage and Options
=================

Create a new directory, subfolders and files in the current directory that will
help quickstart your data science project with packaging, testing, scripts and
other templates.

Usage:
       project_quickstart [--project-name=<project_name> | -n
                              <project_name>] ...
       project_quickstart [--script-python=<script_name>]
       project_quickstart [--script-R=<script_name>]
       project_quickstart [-f | --force]
       project_quickstart [-h | --help]
       project_quickstart [--version]
       project_quickstart [--dry-run]

Options:
    --project-name=DIR -n DIR     Creates a project skeleton
    --script-python=FILE          Create a python script template, '.py' is appended.
    --script-R=FILE               Create an R script template, '.R' is appended.
    -f --force                    Take care, forces to overwrite files and directories.
    -h --help                     Show this screen.
    --version                     Show version.
    --dry-run                     Print to screen only.

Documentation
=============

  For more information see:

      https://github.com/AntonioJBT/project_quickstart

'''
##############################
# Py3 to 2 pasteurize:
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from builtins import map
from builtins import str
from future import standard_library
standard_library.install_aliases()
# Standard Python modules:
import sys
import re
import os
import shutil
import collections
import glob
import string

# Modules with Py2 to 3 conflicts:
try:
    import configparser
except ImportError:  # Py2 to Py3
    import ConfigParser as configparser

try:
    from io import StringIO
except ImportError:  # Python 3
    from io import StringIO

# Modules not in core library:
import docopt

# Package module:
import project_quickstart.projectQuickstart as projectQuickstart
import project_quickstart.version as version

version = version.set_version()

# Get package source directory in (param path) '
src_dir = projectQuickstart.getDir('..')

# For debugging:
#print('project_quickstart package directory is:', '\n', src_dir)

# Global variable for configuration file ('.ini')
# allow_no_value addition is from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# By using `allow_no_value=True` we are allowed to
# write `--force` instead of `--force=true` below.
CONFIG = configparser.ConfigParser(allow_no_value = True)

##############################


##############################
def main():
    ''' with docopt main() expects a dictionary with arguments from docopt()
    docopt will automatically check your docstrings for usage, set -h, etc.
    '''
    options = docopt.docopt(__doc__, version = version)
    welcome_msg = str('\n' + 'Welcome to project_quickstart version {} (!).' +
            '\n').format(version)
    print(welcome_msg)
    docopt_error_msg = str('project_quickstart exited due to an error.' + '\n')
    docopt_error_msg = str(docopt_error_msg
                           + '\n'
                           + 'Try project_quickstart --help'
                           + '\n' + '\n'
                           + 'Options in place:'
                           + '\n'
                           + str(options)
                           + '\n'
                           )

    try:
        # Parse arguments, use file docstring as a parameter definition
        # These arguments are optional
        # help and version are handled automatically by docopt if set in
        # options above.
        # Standard options (log, verbose, version, quiet, dry-run, force):
        if options['--dry-run']:
            print('Dry run, only print what folders will be created.')
            print('Option not in use at the moment')
            pass  # TO DO

        if options['--force']:
            print('Force overwriting directories and files')
            print('Option not in use at the moment')
            pass  # TO DO

        # Programme specific options
        # Required:
        if options['--project-name']:
            project_name = str(options["--project-name"]).strip('[]').strip("''")
            project_root = str('{}').format(project_name)

            # Set up default paths, directoy and file names:                                   
            project_dir = os.path.join(os.getcwd(), project_root)                                                                                
            
            if not os.path.exists(project_dir): 
                os.makedirs(project_dir) 
            
            else: 
                print(docopt_error_msg) 
                print(str('''The directory with the name {} already exists. 
                            Use --force to overwrite.''' 
                            + '\n' 
                            ).format(project_root)) 
                sys.exit() 

        # Addional/alternative if above not given:
        script_template_py = str('template.py') 
        script_template_R = str('template.R')
        
        if options['--script-python'] and len(options['--script-python']) > 0:
            print(''' Copying a Python script template into the current working directory. ''')
            # py3.5 formatting:
            script_name = str(options["--script-python"]).strip('[]').strip("''")
            script_name = str('{}.py').format(script_name)

        elif options['--script-python'] and len(options['--script-python']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to
                  ".py" ''')
            sys.exit()

        if options['--script-R'] and len(options['--script-R']) > 0:
            print(''' Copying an R script template into the current working directory. ''')
            script_name = str(options["--script-R"]).strip('[]').strip("''")
            script_name = str('{}.R').format(script_name)

        elif options['--script-R'] and len(options['--script-R']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to
                  ".R" ''')
            sys.exit()

        # Exit if options not given:
        if (not options['--project-name']
                and not options['--script-R']
                and not options['--script-python']
                ):
            print(docopt_error_msg)
            print('Error in  the options given or none supplied.',
                  '\n',
                  'A project name is required.',
                  'Otherwise you need to use,',
                  '--script-R or --script-python.')
            sys.exit()

    # Handle exceptions:
    except docopt.DocoptExit:
        print(docopt_error_msg)
        raise

    # Get locations of source code
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
    # MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation

    template_dir = projectQuickstart.getDir('../templates') 
    project_template = os.path.join(template_dir, 'project_template')

    def createProject():
        if options['--project-name']:

            dirs_to_use = [template_dir,
                           project_template
                          ]

        # Sanity check:
            for d in dirs_to_use:
                if not os.path.exists(d):
                    print(docopt_error_msg)
                    print(''' The directory:
                               {}
                               does not exist.
                               Are the paths correct? Did the programme install in the
                               right location?
                               'bin' or equivalent dir should be where project_quickstart installed,
                               'templates' and 'project_template' come with this
                               package.
                          '''.format(d))
                    sys.exit()

        # Get the names for the directories to create for the project skeleton:
        manuscript_dir = os.path.join(project_dir, 'manuscript')
        code_dir = os.path.join(project_dir, 'code')
        data_dir = os.path.join(project_dir, 'data')
        results_dir = os.path.join(project_dir, 'results_1')

        dirnames = [manuscript_dir,
                   # code_dir, # leave out as shutil.copytree needs to create the
                   # shutil root dir, otherwise files are not copied
                    data_dir,
                    results_dir
                    ]

        # Sanity check:
        for d in dirnames:
            if os.path.exists(d):
                print(docopt_error_msg)
                print(''' The directory:
                           {}
                           already exists.
                           To overwrite use --force.
                      '''.format(d))
                sys.exit()

        # If directory paths are OK, continue:
        print(str('Paths in use:' + '\n'
                  + template_dir + '\n'
                  + project_template
                  + '\n' + '\n'
                  + 'Creating the project structure for {} in:'.format(project_name) + '\n'
                  + project_dir + '\n')
              )

        # Create directories:
        # TO DO: pass these from ini file
        # Add hardcoded directories first for now:
        dirnames.extend(["{}/raw".format(data_dir)])
        dirnames.extend(["{}/processed".format(data_dir)])
        dirnames.extend(["{}/external".format(data_dir)])

        tree_dir = []
        for d in map(str, dirnames):
            tree_dir = [d for d in list(dirnames)]

            if not os.path.exists(d):
                os.makedirs(d)
            else:
                print(docopt_error_msg)
                print('''The directory {} already exists, use --force to
                        overwrite.'''.format(d))
                sys.exit()

        return(code_dir, manuscript_dir, data_dir, results_dir, tree_dir)

    # Copy files from template directory:
    # TO DO: 'code' dir is hard coded, change to ini parameter later
    # The intention is to use the 'code' dir as a
    # GitHub/packageable directory
    def projectTemplate(src, dst):
        '''
        Copy across project template files for
        a Python/GitHub/etc setup.
        '''
        if os.path.exists(dst) and not options['--force']:
            print(docopt_error_msg)
            raise OSError('''
                          Directory {} already exists - not overwriting.
                          see --help or use --force
                          to overwrite.
                          '''.format(dst)
                          )
            sys.exit()
        else:
            shutil.copytree(src, dst, ignore =
                    shutil.ignore_patterns('.dir_bash*,', '__pycache__*',
                        '*.bak', 'dummy_holder*'))

    # Copy across individual files outside of the 'templates' dir:
    def copySingleFiles(src, dst, string1, string2):
        '''
        Copy the manuscript and lab_notebook templates
        to the 'manuscript' directory and put an initial copy of script
        templates in the project_name/code directory.
        '''
        files = []
        for f in os.listdir(src):
            if string1 in f or string2 in f:
                files.extend([f])
        for f in map(str, files):
            shutil.copy2(os.path.join(src,f), dst)

    # Replace all instances of template with 'name' from project_name as
    # specified in options:
    def renameTree(full_path, old_substring, new_substring):
        '''
        Rename 'template' and 'project_template' strings to name given for new
        project.
        '''
        for dirpath, dirname, filename in os.walk(full_path):
            for d in dirname:
                for f in os.listdir(os.path.join(dirpath, d)):
                    d = os.path.join(dirpath, d)
                    if old_substring in f:
                        os.rename(os.path.join(d, f),
                                  os.path.join(d, f.replace(old_substring,
                                        '{}').format(new_substring))
                                  )

            for d in dirname:
                if old_substring in d:
                    os.rename(os.path.join(str(dirpath), d),
                              os.path.join(str(dirpath), d.replace(
                                  old_substring, '{}').format(new_substring))
                              )

    # Make single copies of script templates as standalone function:
    def scriptTemplate():
        ''' Copy script templates and rename
            them according to option given.
        '''
        cwd = os.getcwd()

        if options['--script-python']:
            copy_to = os.path.join(cwd, script_name)
            if os.path.exists(copy_to) and not options['--force']:
                print(docopt_error_msg)
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_py)
                shutil.copy2(copy_from, copy_to)
                print(copy_to)

        elif options['--script-R']:
            copy_to = os.path.join(cwd, script_name)
            if os.path.exists(copy_to) and not options['--force']:
                print(docopt_error_msg)
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_R)
                shutil.copy2(copy_from, copy_to)
                print(copy_to)
        else:
            print(docopt_error_msg)
            raise ValueError(''' Bad arguments/options used for script template, try --help''')


    # Call functions:
    if options['--project-name']: 
        code_dir, manuscript_dir, data_dir, results_dir, tree_dir = createProject() 
        projectTemplate(project_template, code_dir)
        copySingleFiles(template_dir, manuscript_dir, 'rst', 'rst') 
        copySingleFiles(template_dir, os.path.join(code_dir, 'project_template'), 
                        r'.R', r'.py') 
                                # 'project_template' here refers to                                        
                                #'project_quickstart/templates/project_template' 
                                # directory which will become the user's 
                                # new_project/code/new_project directory 
                                # where scripts can go in 
                                # The code dir can be renamed when uploading 
        renameTree(project_dir, 'project_template', project_name) 
        renameTree(project_dir, 'template', project_name) 

    # Create a script template copy:
    if options['--script-python'] or options['--script-R'] and not options['--project-name']:
        scriptTemplate()

    # Print a nice welcome message (if successful):
    if options['--project-name']:
        end_msg = str( '\n' +
                   """ Done, welcome to {0}!

        The folder structure and files have been successfully copied to
        {1}

        The folder structure is
        {2}

        Remember to back up code, data and manuscript directories (or your
        equivalents).

        The directory
        {3}
        can be uploaded to a version control system (file templates are for GitHub).
        You could link it to Travis CI, Zenodo and ReadtheDocs for example.
        There are some notes and reminders within the files copied over.
        You may want to change the name 'code' to something more suitable when
        uploading, freezing, packaging, etc.

        Script templates are in
        {3}/{0}

        The structure largely follows Python packaging conventions.
        You can put scripts, modules and pipelines (eg Ruffus/CGAT, make and Makefiles, etc.)
        in here.

        You can work and save results in
        {6}

        Install Sphinx to render your rst documents in
        {4}

        Basic rst template files have been generated already.
        Install and use sphinx-quickstart if you want a more complete skeleton.

        Feel free to raise issues, fork or contribute at:

        https://github.com/AntonioJBT/project_quickstart

        Have fun!

        """.format(project_root,
                   project_dir,
                   tree_dir,
                   code_dir,
                   manuscript_dir,
                   data_dir,
                   results_dir
                   )
        )

        print(end_msg)

    return

if __name__ == '__main__':
    # if using docopt:
    # it will check all arguments pass, if not exits with 'Usage
    # if arguments are valid, run the program:
    sys.exit(main())
