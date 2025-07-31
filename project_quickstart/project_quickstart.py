'''
project_quickstart - setup a new python based project
=====================================================

:Author: Antonio Berlanga-Taylor
:Release: |version|
:Date: |date|


Purpose
=======

This script creates a python data science project template. The idea is
to be able to easily turn a project into a package with software testing,
version control, reporting, docs, etc.

Once you've quickstarted your project you can run the --script options to
create python and R script templates or a Ruffus/CGAT pipeline template.

You will need to install other software (e.g. R, Ruffus, Sphinx, etc.) to make
full use depending on your preferences.


Usage and Options
=================

Create a new directory, subfolders and files in the current directory that will
help quickstart your data science project with packaging, testing, scripts and
other templates.

Usage:
       project_quickstart [--project-name=<project_name> | -n <project_name>] ...
       project_quickstart [--script-python=<script_name>]
       project_quickstart [--script-R=<script_name>]
       project_quickstart [--script-pipeline=<pipeline_name>]
       project_quickstart [--example]
       project_quickstart [-f | --force]
       project_quickstart [-h | --help]
       project_quickstart [--version]
       project_quickstart [--dry-run]

Options:
    --project-name=DIR -n DIR     Creates a project skeleton
    --script-python=FILE          Create a python script template, '.py' is appended.
    --script-R=FILE               Create an R script template, '.R' is appended.
    --script-pipeline=FILE        Create a Ruffus/CGAT pipeline template,
                                  'pipeline_FILE.py' is created.
    --example                     Create a project_quickstart example with
                                  runnable scripts and pipeline.
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
# Standard Python modules:
import sys
import os
import shutil
import subprocess

# Modules with Py2 to 3 conflicts:
try:
    import configparser
except ImportError:  # Py2 to Py3
    import ConfigParser as configparser

# Modules not in core library:
import docopt

# Package module:
import project_quickstart.projectQuickstart as projectQuickstart
from project_quickstart.version import __version__ as version

# Get package source directory in (param path) '
src_dir = projectQuickstart.getDir('..')

# For debugging:
# print('project_quickstart package directory is:', '\n', src_dir)

# Global variable for configuration file ('.ini')
# allow_no_value addition is from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# By using `allow_no_value=True` we are allowed to
# write `--force` instead of `--force=true` below.
CONFIG = configparser.ConfigParser(allow_no_value=True)

##############################


##############################
def _project_template(src, dst, *, ignore=(), force=False, error_msg=""):
    """Copy the project template directory."""
    if os.path.exists(dst) and not force:
        print(error_msg)
        raise OSError(
            f"Directory {dst} already exists - not overwriting."
            " see --help or use --force to overwrite."
        )
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*ignore))


def _copy_single_files(src, dst, patterns):
    """Copy files matching patterns from ``src`` into ``dst``."""
    for f in os.listdir(src):
        if any(p in f for p in patterns):
            shutil.copy2(os.path.join(src, f), dst)


def _rename_tree(path, old, new):
    """Rename ``old`` substrings to ``new`` for files and folders below ``path``."""
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for name in list(dirnames) + list(filenames):
            if old in name:
                src = os.path.join(dirpath, name)
                dst = os.path.join(dirpath, name.replace(old, new))
                os.rename(src, dst)


def _make_script(options, script_templates, pipeline_templates, pipeline_name,
                 script_template_py, script_template_R, files_to_ignore,
                 sphinx_configs, sphinx_files, error_msg):
    """Create script or pipeline templates based on CLI options."""
    cwd = os.getcwd()
    if options["--script-python"]:
        copy_to = os.path.join(cwd, options["--script-python"] + ".py")
        if os.path.exists(copy_to) and not options["--force"]:
            print(error_msg)
            raise OSError(
                f"File {copy_to} already exists - not overwriting, "
                "see --help or use --force to overwrite."
            )
        copy_from = os.path.join(script_templates, script_template_py)
        shutil.copy2(copy_from, copy_to)
        print(copy_to)
    elif options["--script-R"]:
        copy_to = os.path.join(cwd, options["--script-R"] + ".R")
        if os.path.exists(copy_to) and not options["--force"]:
            print(error_msg)
            raise OSError(
                f"File {copy_to} already exists - not overwriting, "
                "see --help or use --force to overwrite."
            )
        copy_from = os.path.join(script_templates, script_template_R)
        shutil.copy2(copy_from, copy_to)
        print(copy_to)
    elif options["--script-pipeline"]:
        copy_to = os.path.join(cwd, pipeline_name)
        if os.path.exists(copy_to) and not options["--force"]:
            print(error_msg)
            raise OSError(
                f"Directory {copy_to} already exists - not overwriting, "
                "see --help or use --force to overwrite."
            )
        shutil.copytree(
            pipeline_templates,
            copy_to,
            ignore=shutil.ignore_patterns(*files_to_ignore),
        )
        _copy_single_files(
            sphinx_configs,
            os.path.join(copy_to, "configuration"),
            ["pipeline.yml"],
        )
        _copy_single_files(
            sphinx_configs,
            os.path.join(copy_to, "pipeline_report"),
            sphinx_files,
        )
        _rename_tree(copy_to, "template", options["--script-pipeline"][1:])
        print("Created in:\n", copy_to)


def _create_project_dirs(project_dir, template_dir, py_package_template,
                         report_templates, script_templates, project_name,
                         error_msg):
    """Create the directory skeleton for a project."""

    dirs_to_use = [template_dir, py_package_template, report_templates,
                   script_templates]
    for d in dirs_to_use:
        if not os.path.exists(d):
            print(error_msg)
            print(
                """ The directory: {} does not exist.
                               Are the paths correct? Did the programme install
                               in the right location?
                               'bin' or equivalent dir should be where
                               project_quickstart installed,
                               'templates' and 'project_template' come with this package.
                """.format(d)
            )
            sys.exit()

    manuscript_dir = os.path.join(project_dir, "documents_and_manuscript")
    code_dir = os.path.join(project_dir, "code")
    data_dir = os.path.join(project_dir, "data")
    results_dir = os.path.join(project_dir, "results")

    dirnames = [manuscript_dir, data_dir, results_dir]

    for d in dirnames:
        if os.path.exists(d):
            print(error_msg)
            print(
                """ The directory:
                           {}
                           already exists.
                           To overwrite use --force.
                """.format(d)
            )
            sys.exit()

    print(
        (
            "Path in use:\n" + template_dir + "\n\n"
            + f"Creating the project structure for {project_name} in: \n"
            + project_dir
            + "\n"
        )
    )

    dirnames.extend([f"{data_dir}/raw", f"{data_dir}/processed",
                     f"{data_dir}/external"])

    tree_dir = list(dirnames)
    for d in dirnames:
        os.makedirs(d, exist_ok=True)

    return code_dir, manuscript_dir, data_dir, results_dir, tree_dir


def main(argv=None):
    """Execute the command line interface.

    Parameters
    ----------
    argv : list[str] or None, optional
        Arguments to parse with :func:`docopt.docopt`.  When ``None`` the
        arguments are taken from ``sys.argv`` (the default behaviour of
        ``docopt``).
    """
    options = docopt.docopt(__doc__, argv=argv, version=version)
    welcome_msg = str('\n' + 'Welcome to project_quickstart version {} (!).'
                      + '\n').format(version)
    # print(welcome_msg)
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
            print(welcome_msg)
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
                          ).format(project_root)
                      )
                sys.exit()

        # Addional/alternative command line options:
        script_template_py = str('template.py')
        script_template_R = str('template.R')

        if options['--script-python'] and len(options['--script-python']) > 0:
            print(welcome_msg)
            print(''' Copying a Python script template into the current working directory. ''')
            # py3.5 formatting:
            script_name = str(options["--script-python"]).strip('[]').strip("''")
            script_name = str('{}.py').format(script_name)

        elif options['--script-python'] and len(options['--script-python']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to ".py" ''')
            sys.exit()

        if options['--script-R'] and len(options['--script-R']) > 0:
            print(welcome_msg)
            print(''' Copying an R script template into the current working directory. ''')
            script_name = str(options["--script-R"]).strip('[]').strip("''")
            script_name = str('{}.R').format(script_name)

        elif options['--script-R'] and len(options['--script-R']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a script name. This will be prefixed to ".R" ''')
            sys.exit()

        if options['--script-pipeline'] and len(options['--script-pipeline']) > 0:
            print(welcome_msg)
            print(''' Copying a pipeline template into the current working directory.
                    This includes a Ruffus pipeline.py script template,
                    pipeline yml configuration template for parameters,
                    a report directory with a restructuredText template,
                    and sphinx-quickstart modified conf.py and Makefile files.''')
            pipeline_dir_name = str(options["--script-pipeline"]).strip('[]').strip("''")
            pipeline_dir_name = str('pipeline_{}').format(pipeline_dir_name)
            # All files within the directory
            # project_quickstart/templates/script_templates/pipeline
            # plus
            # project_quickstart/templates/script_templates/pipeline_template.py
            # will get copied over in function below.

        elif options['--script-pipeline'] and len(options['--script-pipeline']) == 0:
            print(docopt_error_msg)
            print(''' You need to provide a pipeline name to generate the
                    directory "pipeline_NAME" ''')
            sys.exit()

        # Exit if options not given:
        if (not options['--project-name']
                and not options['--script-R']
                and not options['--script-python']
                and not options['--script-pipeline']
                and not options['--example']):
            print(docopt_error_msg)
            print('Error in  the options given or none supplied.',
                  '\n',
                  'A project name is required.',
                  'Otherwise you need to use',
                  '--script-R, --script-python or --script-pipeline.')
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
    # MANIFEST.in file instructs the project_quickstart/templates folder to be
    # included in installation

    template_dir = projectQuickstart.getDir('../templates')
    py_package_template = os.path.join(template_dir, 'project_template')
    report_templates = os.path.join(template_dir, 'report_templates')
    script_templates = os.path.join(template_dir, 'script_templates')
    pipeline_templates = os.path.join(script_templates, 'pipeline_template')
    examples_dir = os.path.join(template_dir, 'examples')

    # Modified sphinx-quickstart templates only live in:
    # templates/project_template/docs/
    # but are needed in
    # code/docs, report directory
    # and pipeline directory:
    sphinx_configs = os.path.join(template_dir, 'project_template', 'docs')
    sphinx_files = ['conf.py',
                    'Makefile',
                    'make.bat',
                    'include_links.rst',
                    'index.rst',
                    ]

    files_to_ignore = [
        'dir_bash_history',
        '__pycache__',
        '*.bak',
        'dummy*',
    ]

    if options['--project-name']:
        code_dir, manuscript_dir, data_dir, results_dir, tree_dir = _create_project_dirs(
            project_dir,
            template_dir,
            py_package_template,
            report_templates,
            script_templates,
            project_name,
            docopt_error_msg,
        )

        _project_template(
            py_package_template,
            code_dir,
            ignore=files_to_ignore,
            force=options['--force'],
            error_msg=docopt_error_msg,
        )

        _copy_single_files(
            script_templates,
            os.path.join(code_dir, 'project_template'),
            ['.py', '.R']
        )

        shutil.copytree(
            pipeline_templates,
            os.path.join(code_dir, 'project_template', 'pipeline_template'),
            ignore=shutil.ignore_patterns(*files_to_ignore),
        )

        _copy_single_files(
            sphinx_configs,
            os.path.join(code_dir, 'project_template', 'pipeline_template', 'pipeline_report'),
            sphinx_files,
        )

        _copy_single_files(
            sphinx_configs,
            os.path.join(code_dir, 'project_template', 'pipeline_template', 'configuration'),
            ['pipeline.yml'],
        )

        _copy_single_files(report_templates, manuscript_dir, ['rst'])
        _copy_single_files(sphinx_configs, manuscript_dir, sphinx_files)
        _copy_single_files(template_dir, project_dir, ['rsync', 'TO_DO'])
        _copy_single_files(data_dir, project_dir, ['README_data'])

        _rename_tree(project_dir, 'project_template', project_name)
        _rename_tree(project_dir, 'template', project_name)

    if (options['--script-python']
            or options['--script-R']
            or options['--script-pipeline']
            and not options['--project-name']):
        pipeline_dir_name = None
        if options['--script-pipeline']:
            pipeline_dir_name = f"pipeline_{options['--script-pipeline']}"
        _make_script(
            options,
            script_templates,
            pipeline_templates,
            pipeline_dir_name if pipeline_dir_name else "default_pipeline",
            script_template_py,
            script_template_R,
            files_to_ignore,
            sphinx_configs,
            sphinx_files,
            docopt_error_msg,
        )

    # Print a nice welcome message (if successful):
    if options['--project-name']:
        end_msg = str('\n' + """ Done, welcome to {0}!

        Folders and files have been copied to:
        {1}

        The basic structure is:
                              .
                              |-- code
                              |-- data
                              |-- documents_and_manuscript
                              |-- results

        Remember to back up code, data and manuscript directories (or your equivalents).

        The directory:
        {2}

        can be uploaded to a version control system (file templates are for GitHub).
        You could link it to Travis CI, Zenodo and ReadtheDocs for example.
        There are some notes and reminders within the files copied over.
        You may want to change the name 'code' to something more suitable
        when uploading, freezing, packaging, etc.

        Script templates are in:
        {2}/{0}

        The structure largely follows Python packaging conventions.
        You can put scripts, modules and pipelines (eg Ruffus/CGAT, make and
        Makefiles, etc.) in here.

        You can work and save results in:
        {5}

        Install Sphinx to render your rst documents in:
        {3}

        Basic rst template files have been generated already.
        Install and use sphinx-quickstart if you want a more complete skeleton.

        Feel free to raise issues, fork or contribute at:

        https://github.com/AntonioJBT/project_quickstart

        Have fun!

        """.format(project_root,
                   project_dir,
                   code_dir,
                   manuscript_dir,
                   data_dir,
                   results_dir
                   )
        )

        print(end_msg)

    # Finally, last options to run if specified:
    if options['--example'] and not options['--project-name']:
        pq_exec = shutil.which('project_quickstart')
        if not pq_exec:
            raise FileNotFoundError('project_quickstart executable not found')
        subprocess.run([pq_exec, '-n', 'pq_example'], check=True)
        try:
            shutil.rmtree('pq_example/code/pq_example')
        except FileNotFoundError:
            print("Warning: Directory 'pq_example/code/pq_example' not found. Skipping removal.")
        except PermissionError:
            print("Error: Permission denied while trying to remove 'pq_example/code/pq_example'.")
        except Exception as e:
            print(f"Error: An unexpected issue occurred while removing 'pq_example/code/pq_example': {e}")
        shutil.copytree(
            examples_dir,
            os.path.abspath('pq_example/code/pq_example'),
            ignore=shutil.ignore_patterns(*files_to_ignore),
        )

    return


def create_project(name, *, argv_prefix=None):
    """Programmatically create a project skeleton."""
    args = ["-n", f"{name}"]
    return main(args if argv_prefix is None else argv_prefix + args)


def create_python_script(name, *, argv_prefix=None):
    """Create a standalone Python script template."""
    args = ["--script-python", f"{name}"]
    return main(args if argv_prefix is None else argv_prefix + args)


def create_r_script(name, *, argv_prefix=None):
    """Create a standalone R script template."""
    args = ["--script-R", f"{name}"]
    return main(args if argv_prefix is None else argv_prefix + args)


def create_pipeline(name, *, argv_prefix=None):
    """Create a pipeline template directory."""
    args = ["--script-pipeline", f"{name}"]
    return main(args if argv_prefix is None else argv_prefix + args)


def create_example(*, argv_prefix=None):
    """Generate the example project."""
    args = ["--example"]
    return main(args if argv_prefix is None else argv_prefix + args)


if __name__ == '__main__':
    # if using docopt:
    # it will check all arguments pass, if not exits with 'Usage
    # if arguments are valid, run the program:
    sys.exit(main())
