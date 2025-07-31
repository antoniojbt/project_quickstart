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
import logging

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

# Configure basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# For debugging:
# print('project_quickstart package directory is:', '\n', src_dir)

# Global variable for configuration file ('.ini')
# allow_no_value addition is from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# By using `allow_no_value=True` we are allowed to
# write `--force` instead of `--force=true` below.
CONFIG = configparser.ConfigParser(allow_no_value=True)

##############################

def _welcome_msg():
    return f"\nWelcome to project_quickstart version {version} (!)!\n"


def _docopt_error_msg(options):
    return (
        "project_quickstart exited due to an error.\n\n"
        "Try project_quickstart --help\n\n"
        "Options in place:\n" + str(options) + "\n"
    )


def _end_msg(project_root, project_dir, code_dir, manuscript_dir, data_dir, results_dir):
    return (
        "\n Done, welcome to {0}!\n\n"
        "Folders and files have been copied to:\n{1}\n\n"
        "The basic structure is:\n"
        "                              .\n"
        "                              |-- code\n"
        "                              |-- data\n"
        "                              |-- documents_and_manuscript\n"
        "                              |-- results\n\n"
        "Remember to back up code, data and manuscript directories (or your equivalents).\n\n"
        "The directory:\n{2}\n\n"
        "can be uploaded to a version control system (file templates are for GitHub).\n"
        "You could link it to Travis CI, Zenodo and ReadtheDocs for example.\n"
        "There are some notes and reminders within the files copied over.\n"
        "You may want to change the name 'code' to something more suitable\n"
        "when uploading, freezing, packaging, etc.\n\n"
        "Script templates are in:\n{2}/{0}\n\n"
        "The structure largely follows Python packaging conventions.\n"
        "You can put scripts, modules and pipelines (eg Ruffus/CGAT, make and Makefiles, etc.) in here.\n\n"
        "You can work and save results in:\n{5}\n\n"
        "Install Sphinx to render your rst documents in:\n{3}\n\n"
        "Basic rst template files have been generated already.\n"
        "Install and use sphinx-quickstart if you want a more complete skeleton.\n\n"
        "Feel free to raise issues, fork or contribute at:\n\n"
        "https://github.com/AntonioJBT/project_quickstart\n\n"
        "Have fun!\n"
    ).format(
        project_root,
        project_dir,
        code_dir,
        manuscript_dir,
        data_dir,
        results_dir,
    )




##############################
def _project_template(src, dst, *, ignore=(), force=False, error_msg=""):
    """Copy the project template directory."""
    if os.path.exists(dst) and not force:
        logger.error(error_msg)
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
            logger.error(error_msg)
            raise OSError(
                f"File {copy_to} already exists - not overwriting, "
                "see --help or use --force to overwrite."
            )
        copy_from = os.path.join(script_templates, script_template_py)
        shutil.copy2(copy_from, copy_to)
        logger.info(copy_to)
    elif options["--script-R"]:
        copy_to = os.path.join(cwd, options["--script-R"] + ".R")
        if os.path.exists(copy_to) and not options["--force"]:
            logger.error(error_msg)
            raise OSError(
                f"File {copy_to} already exists - not overwriting, "
                "see --help or use --force to overwrite."
            )
        copy_from = os.path.join(script_templates, script_template_R)
        shutil.copy2(copy_from, copy_to)
        logger.info(copy_to)
    elif options["--script-pipeline"]:
        copy_to = os.path.join(cwd, pipeline_name)
        if os.path.exists(copy_to) and not options["--force"]:
            logger.error(error_msg)
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
        logger.info("Created in:\n%s", copy_to)


def _create_project_dirs(project_dir, template_dir, py_package_template,
                         report_templates, script_templates, project_name,
                         error_msg):
    """Create the directory skeleton for a project."""

    dirs_to_use = [template_dir, py_package_template, report_templates,
                   script_templates]
    for d in dirs_to_use:
        if not os.path.exists(d):
            logger.error(error_msg)
            logger.error(
                " The directory: %s does not exist.\n"
                "Are the paths correct? Did the programme install\n"
                "in the right location? 'bin' or equivalent dir should be where\n"
                "project_quickstart installed, 'templates' and 'project_template' come with this package.",
                d,
            )
            sys.exit()

    manuscript_dir = os.path.join(project_dir, "documents_and_manuscript")
    code_dir = os.path.join(project_dir, "code")
    data_dir = os.path.join(project_dir, "data")
    results_dir = os.path.join(project_dir, "results")

    dirnames = [manuscript_dir, data_dir, results_dir]

    for d in dirnames:
        if os.path.exists(d):
            logger.error(error_msg)
            logger.error(
                " The directory: %s already exists. To overwrite use --force.",
                d,
            )
            sys.exit()

    logger.info(
        "Path in use:\n%s\n\nCreating the project structure for %s in:\n%s\n",
        template_dir,
        project_name,
        project_dir,
    )

    dirnames.extend([f"{data_dir}/raw", f"{data_dir}/processed",
                     f"{data_dir}/external"])

    tree_dir = list(dirnames)
    for d in dirnames:
        os.makedirs(d, exist_ok=True)

    return code_dir, manuscript_dir, data_dir, results_dir, tree_dir


def parse_cli(argv=None):
    """Parse command line arguments."""
    return docopt.docopt(__doc__, argv=argv, version=version)


def validate_options(options):
    """Validate command line options."""
    if not (
        options['--project-name']
        or options['--script-R']
        or options['--script-python']
        or options['--script-pipeline']
        or options['--example']
    ):
        raise ValueError(
            'A project name is required or use --script-*/--example to generate templates.'
        )


def handle_project_creation(options, template_dir, py_package_template,
                            report_templates, script_templates, pipeline_templates,
                            sphinx_configs, sphinx_files, files_to_ignore,
                            error_msg):
    project_name = str(options["--project-name"]).strip('[]').strip("''")
    project_root = f"{project_name}"
    project_dir = os.path.join(os.getcwd(), project_root)

    if os.path.exists(project_dir):
        raise FileExistsError(
            f"The directory with the name {project_root} already exists. Use --force to overwrite."
        )

    os.makedirs(project_dir)

    code_dir, manuscript_dir, data_dir, results_dir, tree_dir = _create_project_dirs(
        project_dir,
        template_dir,
        py_package_template,
        report_templates,
        script_templates,
        project_name,
        error_msg,
    )

    _project_template(
        py_package_template,
        code_dir,
        ignore=files_to_ignore,
        force=options['--force'],
        error_msg=error_msg,
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

    return project_root, project_dir, code_dir, manuscript_dir, data_dir, results_dir


def handle_script_generation(options, script_templates, pipeline_templates,
                             sphinx_configs, sphinx_files, files_to_ignore,
                             error_msg):
    pipeline_dir_name = None
    if options['--script-pipeline']:
        pipeline_dir_name = f"pipeline_{options['--script-pipeline']}"

    _make_script(
        options,
        script_templates,
        pipeline_templates,
        pipeline_dir_name if pipeline_dir_name else "default_pipeline",
        'template.py',
        'template.R',
        files_to_ignore,
        sphinx_configs,
        sphinx_files,
        error_msg,
    )


def run_example(examples_dir, files_to_ignore):
    pq_exec = shutil.which('project_quickstart')
    if not pq_exec:
        raise FileNotFoundError('project_quickstart executable not found')
    subprocess.run([pq_exec, '-n', 'pq_example'], check=True)
    try:
        shutil.rmtree('pq_example/code/pq_example')
    except FileNotFoundError:
        logger.warning("Directory 'pq_example/code/pq_example' not found. Skipping removal.")
    except PermissionError:
        logger.error("Permission denied while trying to remove 'pq_example/code/pq_example'.")
    except Exception as e:
        logger.error("Unexpected issue removing 'pq_example/code/pq_example': %s", e)
    shutil.copytree(
        examples_dir,
        os.path.abspath('pq_example/code/pq_example'),
        ignore=shutil.ignore_patterns(*files_to_ignore),
    )


def main(argv=None):
    """Execute the command line interface."""
    options = parse_cli(argv)
    try:
        validate_options(options)
    except ValueError:
        logger.error(_docopt_error_msg(options))
        raise

    if options['--dry-run']:
        logger.info('Dry run, only print what folders will be created.')

    if options['--force']:
        logger.info('Force overwriting directories and files')

    template_dir = projectQuickstart.getDir('../templates')
    py_package_template = os.path.join(template_dir, 'project_template')
    report_templates = os.path.join(template_dir, 'report_templates')
    script_templates = os.path.join(template_dir, 'script_templates')
    pipeline_templates = os.path.join(script_templates, 'pipeline_template')
    examples_dir = os.path.join(template_dir, 'examples')

    sphinx_configs = os.path.join(template_dir, 'project_template', 'docs')
    sphinx_files = ['conf.py', 'Makefile', 'make.bat', 'include_links.rst', 'index.rst']

    files_to_ignore = ['dir_bash_history', '__pycache__', '*.bak', 'dummy*']

    project_paths = None

    if options['--project-name']:
        logger.info(_welcome_msg().strip())
        project_paths = handle_project_creation(
            options,
            template_dir,
            py_package_template,
            report_templates,
            script_templates,
            pipeline_templates,
            sphinx_configs,
            sphinx_files,
            files_to_ignore,
            _docopt_error_msg(options),
        )

    if (
        options['--script-python']
        or options['--script-R']
        or options['--script-pipeline']
    ) and not options['--project-name']:
        handle_script_generation(
            options,
            script_templates,
            pipeline_templates,
            sphinx_configs,
            sphinx_files,
            files_to_ignore,
            _docopt_error_msg(options),
        )

    if options['--project-name'] and project_paths:
        end_msg = _end_msg(*project_paths)
        logger.info(end_msg)

    if options['--example'] and not options['--project-name']:
        run_example(examples_dir, files_to_ignore)

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
