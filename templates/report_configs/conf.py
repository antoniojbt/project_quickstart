#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
# NOTE! #
# project documentation build configuration file
# This file is a template copy
# Run sphinx-quickstart to start from scratch
###################################################


######################
# This file is execfile()d with the current directory set to its
# containing dir.

# Note that not all possible configuration values are present in this
# autogenerated file.

# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
######################


# Needed for docstrings:
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
#from future import standard_library
#standard_library.install_aliases()
import os
import sys
import re
import fnmatch

# Get location to this file:
here = os.path.abspath(os.path.dirname(__file__))
print(here)

# Set up calling parameters from INI file:
# Modules with Py2 to 3 conflicts
try:
    import configparser
except ImportError:  # Py2 to Py3
    import ConfigParser as configparser

# Global variable for configuration file ('.ini')
# allow_no_value addition is from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# By using `allow_no_value=True` we are allowed to
# write `--force` instead of `--force=true` below.
CONFIG = configparser.ConfigParser(allow_no_value = True)

count = 0
for f in os.listdir('.'):
    if fnmatch.fnmatch(f, '*.ini'):
        count += 1
        ini_file = f
        print(f)
    else:
        sys.exit('No ini file found, please create one, manually edit or
                regenerate the conf.py file')
if count > 1:
    sys.exit('Error, you have more than one ini file, you will need to
              edit conf.py manually or create a new one to generate the
              documentation or report')
else:
    ini_file = f

CONFIG.read(os.path.join(here, ini_file))

# Print keys (sections):
print('Values for setup.py:', '\n')
for key in CONFIG:
    for value in CONFIG[key]:
        print(key, value, CONFIG[key][value])
#################


#################
# Get version:
#sys.path.insert(0, here)
#src_dir = str(CONFIG['metadata']['project_name'] + '/' + CONFIG['metadata']['project_name'])
src_dir = str(CONFIG['metadata']['project_name'])
sys.path.insert(0, src_dir)
print(src_dir)

import version

version = version.set_version()
print(version)
#################


#################
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = CONFIG['metadata']['project_name']
copyright = CONFIG['metadata']['year'], CONFIG['metadata']['author_name']
author = CONFIG['metadata']['author_name']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.dir_bash_history']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = |project_name|'doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc,
                    str(CONFIG['metadata']['project_name'] + '.tex'),
                    str(CONFIG['metadata']['project_name'] + 'Documentation'),
                    CONFIG['metadata']['author_name'],
                    'manual'),
                    ]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc,
              CONFIG['metadata']['project_name'],
              str(CONFIG['metadata']['project_name'] + ' Documentation'),
              [author], 1)
              ]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(master_doc,
                      str(CONFIG['metadata']['project_name']),
                      str(CONFIG['metadata']['project_name'] + ' Documentation'),
                      author,
                      CONFIG['metadata']['project_name'],
                      str(CONFIG['metadata']['short_description'],
                      'Miscellaneous'),
                      ]

# This is from CGAT to include/exclude in docs depending on PARAMS used:
# Added from some notes I had, maybe CGAT:
#def setup(app):
#     from sphinx.util.texescape import tex_replacements
#     tex_replacements += [(u'♮', u'$\\natural$'),
#                          (u'ē', u'\=e'),
#                          (u'♩', u'\quarternote'),
#                          (u'↑', u'$\\uparrow$'),
#]
#################
