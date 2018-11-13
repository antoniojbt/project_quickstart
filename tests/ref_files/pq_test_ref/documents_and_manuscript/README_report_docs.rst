############################
README for the report folder
############################

The folder structure and templates are setup with restructuredText and Sphinx
as the main tools for creating and rendering documents (PDFs, HTMLs, etc.).

Running project_quickstart -n project_XXXX will copy configuration files generated
from a basic sphinx-quickstart run:

- make.bat
- Makefile
- conf.py

These were modified to include rst substitution variables such as project_name and author_name.

These will also be copied if running project_quickstart --script-pipeline=NAME
Templates such as a manuscript and cover letter are also included, or some
equivalents for reporting in the pipeline_NAME directory.

Templates and config files are from a basic setup to get started faster. 
You can ignore, delete or regenerate them. Use sphinx-quickstart, pandoc, or other renderers.

There is a template for rst substitution variables as well. Manual checking and editing 
are needed of course:

index.rst
include_links.rst
report_substitution_vars.rst
rst_substitution_instructions.rst

After creating the project skeleton with project_quickstart, do:

.. code-block::

	make html
	ln -s _build/html/index.hmtl .
	make latexpdf
	ln -s _build/latex/project_XXXX.pdf .

These commands need to be run where the conf.py and other Sphinx templates are,
usually:

- project_XXXX/code/docs for the code documentation
- project_XXXX/documents_and_manuscript/ for the manuscript preparation
- project_XXXX/results/pipeline_XXXX/report_pipeline_XXX

index.rst (or other rst file) is used as the master document, simply
include all file names to be rendered there.

For images you see:

http://www.sphinx-doc.org/en/stable/rest.html

http://www.sphinx-doc.org/en/stable/builders.html#builders

use e.g.: my_figure.* so that sphinx can choose which format is the most
appropriate conversion (html, pdf).

For SVG files, have the Makefile convert svg to pdf before running Sphinx, see:

https://sites.google.com/site/nickfolse/home/sphinx-latexpdf-output-with-svg-images


