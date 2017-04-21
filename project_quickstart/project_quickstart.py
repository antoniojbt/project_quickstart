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
control, reporting, docs, etc. The package can be kept private, made public,
etc. Even if the code is project specific it can still be versioned, frozen and
archived for reproducibility purposes later on. This tool has the following in
mind:

    Reproducibility concepts and best practice
    Ruffus as a pipeline tool and CGAT tools for support
    Python programming and packaging
    restructuredText and Sphinx for reporting
    Travis and tox for testing
    Conda and Docker for management and development
    GitHub for version control

I've additionally put some basic instructions/reminders to link GitHub with:

    ReadtheDocs (to easily render your documentation online)
    Zenodo (for archiving your code and generating a DOI)
    Travis CI (to integratecode testing)

Once you've quickstarted your project you can run run the --script options to
create python and R script templates.

For a pipeline quickstart based on a Ruffus and CGAT framework see also:
https://github.com/CGATOxford/CGATPipelines/blob/master/scripts/pipeline_quickstart.py
(on which this code is based on)

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
       project_quickstart [--update | -u]
       project_quickstart [--script-python=<script_name>]
       project_quickstart [--script-R=<script_name>]
       project_quickstart [-f | --force]
       project_quickstart [-h | --help]
       project_quickstart [--version]
       project_quickstart [--quiet]
       project_quickstart [--verbose]
       project_quickstart [--log=<log_file> | -L <log_file>]
       project_quickstart [--dry-run]

Options:
    --project-name=DIR -n DIR     Creates a project skeleton
    --update -u                   Propagate changes made in project_quickstart.ini
    --script-python=FILE          Create a python script template, '.py' is appended.
    --script-R=FILE               Create an R script template, '.R' is appended.
    -f --force                    Take care, forces to overwrite files and directories.
    -h --help                     Show this screen.
    --version                     Show version.
    --quiet                       Print less text.
    --verbose                     Print more text.
    -L FILE --log=FILE            Log file name. [default: project_quickstart.log]
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
    import configparser as configparser

try:
    from io import StringIO
except ImportError:  # Python 3
    from io import StringIO

# Modules not in core library:
import docopt

# Package module:
import project_quickstart.projectQuickstart as projectQuickstart
import project_quickstart.version as version

version = version.__version__

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
    welcome_msg = str('Welcome to project_quickstart (!)' + '\n')
    print(welcome_msg)
    docopt_error_msg = str('project_quickstart exited due to an error:')
    docopt_error_msg = str(docopt_error_msg
                           + '\n'
                           + 'Try project_quickstart --help'
                           + '\n'
                           + 'Options in place:'
                           + '\n'
                           + str(options)
                           + '\n'
                           )

    try:
        # Parse arguments, use file docstring as a parameter definition
        # These arguments are optional
        # Standard options (log, verbose, version, quiet, dry-run, force):
        if not options['--log']:
            log = str(CONFIG['metadata']['project_name'] + '.log')
            pass  # TO DO, script log function
        else:
            log = str(options["--log"]).strip('[]').strip("''")

        if options['--verbose']:
            print('Option not in use at the moment')
            pass  # TO DO

#        if options['--version']:
#            print(version) #CONFIG['metadata']['version']

        if options['--quiet']:
            print('Option not in use at the moment')
            pass  # TO DO

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

        # Addional/alternative if above not given:
        if options['--update']:
            print('Option not in use at the moment')
            # Get ini file to read values from:                                                   
            INI_file = projectQuickstart.getINIdir()

            if os.path.isfile(INI_file):
                print('There is an INI configuration file in:', '\n', INI_file, '\n')
                # Read values from the INI file:                                                   
                CONFIG.read(INI_file)
                for key in CONFIG:
                    for value in CONFIG[key]:
                        print(key, value, CONFIG[key][value])

            else:
                print('After manually editing the ini file run --update ',
                      'to propagate the changes.')
                sys.exit()
                # TO DO

        if options['--script-python'] and len(options['--script-python']) > 0:
            print(''' Creating a Python script template. A softlink is
                  created in the current working directory and the
                  actual file in new_project/code/new_project/ ''')
            # py3.5 formatting:
            script_name = str(options["--script-python"]).strip('[]').strip("''")
            script_name = str('{}.py').format(script_name)
            print(script_name)
        elif options['--script-python'] and len(options['--script-python']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to
                  ".py" ''')
            sys.exit()

        if options['--script-R'] and len(options['--script-R']) > 0:
            print(''' Creating an R script template. A softlink is
                  created in the current working directory and the
                  actual file in new_project/code/new_project/ ''')
            script_name = str(options["--script-R"]).strip('[]').strip("''")
            script_name = str('{}.R').format(script_name)
            print(script_name)
        elif options['--script-R'] and len(options['--script-R']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to
                  ".R" ''')
            sys.exit()

        # Exit if options not given:
        if (not options['--project-name']
                and not options['--update']
                and not options['--script-R']
                and not options['--script-python']
                ):
            print(docopt_error_msg)
            print('Error in  the options given or none supplied.',
                  '\n',
                  'A project name is required. ',
                  'Otherwise you need to use --update, ',
                  '--script-R or --script-python for example.')
            sys.exit()

    # Handle exceptions:
    except docopt.DocoptExit:
        print(docopt_error_msg)
        raise

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

    # Get locations of source code
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
    # MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation

    template_dir = projectQuickstart.getDir('../templates')
    project_template = os.path.join(template_dir, 'project_template')

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
    script_template_py = str('template.py')
    script_template_R = str('template.R')

    dirnames = [manuscript_dir,
               # code_dir, # leave out as shutil.copytree needs to create the
               # shutit root dir, otherwise files are not copied
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
                   '''.format(dir_path))
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

    # Copy files from template directory:
    def projectTemplate(src, dst):
        '''
        Copy across project template files for
        a Python/GitHub/etc setup.
        TO DO: 'code' dir is hard coded, change to ini parameter later
        The intention is to use the 'code' dir as a
        GitHub/packageable directory
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
                        '*.bak'))

    projectTemplate(project_template, code_dir)

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

    copySingleFiles(template_dir, manuscript_dir, 'rst', 'rst')
    copySingleFiles(template_dir, os.path.join(code_dir, project_root), r'.R',
                    r'.py')

    # Replace all instances of template with 'name' from project_name as
    # specified in options:
    def renameTree(full_path, old_substring, new_substring):
        '''
        rename 'template' and 'project_template' strings to name given for new
        project
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
    renameTree(project_dir, 'project_template', project_name)
    renameTree(project_dir, 'template', project_name)

# TO DO: how to find the data python package file? See above, check CGAT
# example.
    def scriptTemplate():
        ''' Copy script templates and rename
            them according to option given
        '''
        code_dir = getDir('code')
        print(code_dir)
        if options['--script-python']:
           # copy_to = os.path.join(code_dir, 'scripts', str(script_name + '.py'))
            copy_to = os.path.join(os.path.dirname(), str(script_name + '.py'))
            if os.path.exists(copy_to) and not options['--force']:
                print(docopt_error_msg)
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_py)
                shutil.copy2(copy_from, copy_to)
                #os.rename(os.path.join(copy_to, script_template_py),
                #          filename.replace('template', {})).format(script_name)
                os.symlink(copy_to, os.getcwd())

        elif options['--script-R']:
            copy_to = os.path.join(code_dir, project_root, str(script_name + '.R'))
            if os.path.exists(copy_to) and not options['--force']:
                print(docopt_error_msg)
                raise OSError(''' File {} already exists - not overwriting,
                              see --help or use --force to overwrite.
                              '''.format(script_name)
                              )
            else:
                copy_from = os.path.join(template_dir, script_template_R)
                shutil.copy2(copy_from, copy_to)
               # os.rename(os.path.join(copy_to, script_template_R),
               #           filename.replace('template',
               #                            {})).format(script_name)
                os.symlink(copy_to, os.getcwd())

        else:
            print(docopt_error_msg)
            raise ValueError(''' Bad arguments/options used for script template,
            try --help''')

    if options['--script-python'] or options['--script-R']:
        scriptTemplate()

    # Print a nice welcome message (if successful):
    print(str( '\n' +
               """ Done, welcome to {0}!

    The folder structure and files have been successfully copied to
    {1}/

    Files have been copied 'as is'. You can edit the configuration file
    ({0}.ini, for python packaging) and run:

    python project_quickstart --update

    to update files with your chosen parameters (note that some files can get
    overwritten).

    The folder structure is
    {2}/

    Remember to back up code, data and manuscript directories (or your equivalent).

    The directory
    {3}/
    can be uploaded to a version control system for example
    (file templates are for GitHub). Link to Travis CI, Zenodo and
    ReadtheDocs (notes and reminders within the files copied over)

    Script templates are in
    {3}/{0}/

    The structure largely follows Python packaging conventions.
    You can put scripts, modules and pipelines (eg Ruffus/CGAT, make and Makefiles, etc.)
    in here.

    You can work and save results in
    {6}/

    Install Sphinx to render your rst documents in
    {4}/

    Basic rst template files have been generated already.
    Install and use sphinxqhickstart if you want a more complete skeleton.

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
    ))

    return

if __name__ == '__main__':
    # if using docopt:
    # it will check all arguments pass, if not exits with 'Usage
    # if arguments are valid, run the program:
    sys.exit(main())
