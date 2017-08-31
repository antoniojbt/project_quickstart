'''
Utilities for project_quickstart.py

:Author: Antonio J Berlanga-Taylor
:Date: |date|


Boilerplate tools for quickstarting a data analysis project:

https://github.com/AntonioJBT/project_quickstart

'''

#################
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
import os
import sys

# Set up calling parameters from INI file:
# Modules with Py2 to 3 conflicts
try:
    import configparser
except ImportError:  # Py2 to Py3
    import ConfigParser as configparser
# Global variable for configuration file ('.ini'):
CONFIG = configparser.ConfigParser(allow_no_value = True)

# Modules not in core library:
import docopt

# Define options according to docopt:
options = docopt.docopt(__doc__, version = version)
#################


################# 
cwd = os.getcwd()
def getINIdir(path = cwd):
    ''' Search for an INI file, default is where the current working directory '''
    f_count = 0
    for f in os.listdir(path):
        if (f.endswith('.ini') and not f.startswith('tox')):
            f_count += 1
            INI_file = f
    if f_count == 1:
        INI_file = os.path.abspath(os.path.join(path, INI_file))
    elif (f_count > 1 or f_count == 0):
        INI_file = os.path.abspath(path)
        print('You have no project configuration (".ini") file or more than one',
              'in the directory:', '\n', path)

    return(INI_file)
################# 


#################
# Get locations of source code
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
# MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation

_ROOT = os.path.abspath(os.path.dirname(__file__))
def getDir(path = _ROOT):
    ''' Get the absolute path to where this function resides. Useful for
    determining the user's path to a package. If a sub-directory is given it
    will be added to the path returned. Use '..' to go up directory levels. '''
   # src_top_dir = os.path.abspath(os.path.join(_ROOT, '..'))
    src_dir = _ROOT
    return(os.path.abspath(os.path.join(src_dir, path)))
#################


#################
def createProject():
    if options['--project-name']:

        dirs_to_use = [template_dir,
                       py_package_template,
                       report_templates,
                       script_templates
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
    manuscript_dir = os.path.join(project_dir, 'documents_and_manuscript')
    code_dir = os.path.join(project_dir, 'code')
    data_dir = os.path.join(project_dir, 'data')
    results_dir = os.path.join(project_dir, 'results')

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
    print(str('Path in use:' + '\n'
              + template_dir + '\n'
              #+ py_package_template
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
#################


#################
def projectTemplate(src, dst):
    '''
    Copy across project template files for
    a Python/GitHub/etc setup.
    Files {} are ignored.
    '''.format(files_to_ignore)

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
        shutil.copytree(src,
                        dst,
                        ignore = shutil.ignore_patterns(*files_to_ignore)
                        )
#################


#################
# Copy across individual files outside of the 'templates' dir:
def copySingleFiles(src, dst, *args):
    '''
    Copies named files into the current working directory
    from a given directory excluding
    {}
    '''.format(files_to_ignore)

    files = []
    for f in os.listdir(src):
        for arg in args:
            if arg in f:
                files.extend([f])
            else:
                pass
        #for i in files_to_ignore:
        #    for f in files:
        #        if i in f:
        #            files.remove([f])
        #        else:
        #            pass
    for f in map(str, files):
        shutil.copy2(os.path.join(src, f),
                     dst
                     )
#################



#################
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
        # Files in the root dir called don't get renamed, run here:     
        for f in os.listdir(dirpath):
            if old_substring in f:
                os.rename(os.path.join(dirpath, f),
                          os.path.join(dirpath, f.replace(old_substring,
                                '{}').format(new_substring))
                          )
#################


#################
# Make single copies of script templates as standalone function:
def scriptTemplate():
    ''' Copy script templates and rename
        them according to option given.
        For pipeline option this creates a directory
        with a Ruffus pipeline script template, ini parameters
        file and sphinx-quickstart modified templates.
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
            copy_from = os.path.join(script_templates, script_template_py)
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
            copy_from = os.path.join(script_templates, script_template_R)
            shutil.copy2(copy_from, copy_to)
            print(copy_to)

    elif options['--script-pipeline']:
        copy_to = os.path.join(cwd, pipeline_dir_name)
        if os.path.exists(copy_to) and not options['--force']:
            print(docopt_error_msg)
            raise OSError(''' A directory with the name given
                              {}
                              already exists - not overwriting,
                              see --help or use --force to overwrite.
                          '''.format(copy_to)
                          )
        else:
            shutil.copytree(pipeline_templates,
                            copy_to,
                            ignore = shutil.ignore_patterns(*files_to_ignore)
                           )
            # Copy sphinx-quickstart config files:
            copySingleFiles(sphinx_configs,
                            copy_to,
                            *sphinx_files)
            # Rename all 'template' substrings:
            pipeline_name = str(pipeline_dir_name).strip('pipeline_')
            renameTree(copy_to,
                       'template',
                       pipeline_name
                       )
            print('Created in:', '\n',
                  copy_to)

    else:
        print(docopt_error_msg)
        raise ValueError(''' Bad arguments/options used for script template, try --help''')
#################
