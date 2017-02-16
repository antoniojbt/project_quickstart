####
Plan 
####

:Date: 20 January 2017
:Author: Antonio B 

Current state
#############

- B with T and E

- Wrap pipe quickstart

Future work
###########


TO DO
#####

- project_quickstart/scripts/project_quickstart.py basically just copies the contents of project_quickstart/templates/python_packaging.dir/ so as to have all the skeleton files needed for:
	+ Github repository files (but not .git) like: .gitignore, README, THANKS, TODO, LICENCE, etc.
	+ Travis testing files, tests dir with skeleton files
	+ Tox python testing: TODO: https://tox.readthedocs.io/en/latest/
	+ Python packaging files
	+ Dockerfile
	+ etc
	+ Zenodo? See: zenodo_ github guide. It's easy: allow permissions and then with each tag release zenodo archives the repo and gives it a DOI. See also SSI blog_ on zenodo.
	
.. _zenodo: https://guides.github.com/activities/citable-code/
	
.. _blog: https://www.software.ac.uk/blog/2016-09-26-making-code-citable-zenodo-and-github
	
	+ conda? See: bioconda_, contributing a recipe_ and guidelines_.
	
.. _bioconda: https://bioconda.github.io/index.html
	
.. _recipe: https://bioconda.github.io/contribute-a-recipe.html
	
.. _guidelines: https://bioconda.github.io/guidelines.html

- project_quickstart/scripts/script_quickstart.py copies project_quickstart/templates/template.py or template.R
- project_quickstart/scripts/project_quickstart.py creates a folder structure with file templates for a data science project:
	+ data
	+ code
	+ results
	+ manuscript
	+ etc. these can be specified in the PARAMS.ini file
	+ See this layout_ explanation
	
.. _layout: https://www.cgat.org/downloads/public/cgatpipelines/documentation/Reference.html#term-pipeline-scripts

- See some notes in cgat reports_.

.. _reports: https://www.cgat.org/downloads/public/cgatpipelines/documentation/PipelineReports.html#writingreports


- Pass variables such as project name, author, date, etc. automatically to the various files that need them (setup.py, Dockerfile, manuscript_template, ... )

- Project workflow! e.g.::
	1. run this package to setup folders, github repo structure, code testing, py package files, etc.
	1a. Download packages, tools, etc. Setup Docker, conda kaspel, or other form of tracking environment, packages and their versions.
    1b. Manually connect GitHub with integrated services (Travis CI, Zenodo,
    RTD).
	2. code and test code with tox, travis and py.test
	3. analyse, ...
	4. create new scripts, new pipelines, test them
	5. document code as you go, update with sphinx autodoc
	6. generate internal report with plots, text, etc.
	7. freeze with release tag + zenodo archiving and/or tar ball with py sdist
	8. Repeat cycle

- Mirror local to remote?
    + Have dedicated test_data dir (to mirror). Inside code_dir in tests dir?
    + 

- Testing:
	+ See tox, travis and py.test for a proper setup of py virtualenv, CI and unit testing respectively.
	+ Check travis setup, is pep8 running? flake8 gives errors and log at travis
	+ See CGAT docs for testing_
	
	.. _testing: https://www.cgat.org/downloads/public/cgat/documentation/testing.html#testing
	
	+ Add Travis tests for R


- Update external dependencies file, see some help here_. Consider using pyup.io for alerts on package updates?

.. _here: https://www.cgat.org/downloads/public/cgat/documentation/modules/Requirements.html

- Keep track of installations for Docker. Check conda kapsel_ and here_.

.. _kapsel: https://conda.io/docs/kapsel/

.. _here: https://github.com/conda/kapsel


- Add a project checklist template (eg with comp bio best practice checklist, conda recipe, zenodo deposit, etc.)

- Add python docs with rst/sphinx and doctests, see sphinx_, quickstart_ and doctests_.
- See this tutorial_ for Sphinx and general python packaging/workflow 

.. _tutorial: https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

.. _sphinx: http://www.sphinx-doc.org/en/stable/

.. _quickstart: http://thomas-cokelaer.info/tutorials/sphinx/quickstart.html

.. _doctests: http://thomas-cokelaer.info/tutorials/sphinx/doctest.html

- Check PyPi as a repository for pip install and conda recipe. Check python's cheesecake for sanity checking before
uploading to PyPi

- Use releases as code freezes

- Style: have a look at cgat style_ example which also includes info 

.. _style: https://www.cgat.org/downloads/public/cgat/documentation/styleguide.html#styleguide

- Add R's sessionInfo() and python and shell env equivalents to logs (pip freeze?, conda list, etc.).

- Have methods and plot scripts output legend\*.rst with parameters used, method\*.rst and generic interpretation\*.rst files output to disk to then glob into manuscript template.

- Fix readthedocs 'too many symbolic links'. How to link root dir rst files to docs dir for github? See here_ for a different solution.

.. _here: https://daler.github.io/sphinxdoc-test/includeme.html

- rst rendering gives different results in github vs locally with sphinx

- Sort out pdf local rendering with rst2pdf, make pdflatex, etc.

- Main script works: sort out path finding, --update, --script

-- Sort out: --log, --dry-run, --force, --quiet, --verbose, all these can be
done with CGAT. See conflict with docopt and parsing.

- Automatically run pipeline_quickstart.py at project creation?

- Clean up templates dir: script names, files to add?, improve templates from
  proj_quickstart example.
PIPELINE PLAN
#############

.. todo::
	TO DO: scan/ppt pipeline workflow plus notes

-----


The output should be input for:


References
##########

Also see:
