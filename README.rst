.. image:: https://travis-ci.org/AntonioJBT/project_quickstart.svg?branch=master
   :target: https://travis-ci.org/AntonioJBT/project_quickstart

.. image:: https://readthedocs.org/projects/project-quickstart/badge/?version=latest
   :target: http://project-quickstart.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


##################
Project Quickstart
##################

Boilerplate tools and templates for setting up a data analysis project.

Create a new directory, subfolders and files that will help quickstart your data science project with packaging, testing, scripts, reporting and other templates.

Even if the code is project specific it can still be versioned, frozen and archived for reproducibility purposes later on.

This tool was produced with the following in mind:

- Reproducibility concepts and best practice implementation
- Use of Ruffus_ as a pipeline tool and CGAT_ tools for support 
- Python_ programming and packaging_
- restructuredText_ and Sphinx_ for reporting
- Travis_ and tox_ for testing
- Conda_ and Docker_ for management and development
- GitHub_ for version control

I've additionally put some basic instructions/reminders to link GitHub with:

- ReadtheDocs_ (to easily render your documentation online)
- Zenodo_ (for archiving your code and generating a DOI)
- Travis CI (to integrate code testing)

.. _Ruffus: http://www.ruffus.org.uk/

.. _CGAT: http://www.cgat.org/cgat/Tools/the-cgat-code-collection

.. _Python: https://www.python.org/

.. _packaging: https://packaging.python.org/

.. _restructuredText: http://docutils.sourceforge.net/rst.html

.. _Sphinx: http://www.sphinx-doc.org/en/stable/

.. _Travis: https://travis-ci.org/

.. _tox: https://tox.readthedocs.io/en/latest/

.. _Conda: http://conda.pydata.org/docs/#

.. _Docker: https://www.docker.com/
.. _GitHub: https://github.com/

.. _ReadtheDocs: https://readthedocs.org/

.. _Zenodo: https://guides.github.com/activities/citable-code/


You can later on build computational pipelines using for example a pipeline quickstart tool based on a `Ruffus and CGAT framework`_.

.. _`Ruffus and CGAT framework`: https://github.com/CGATOxford/CGATPipelines/blob/master/scripts/pipeline_quickstart.py

You will need to install other software (e.g. R, Ruffus, Sphinx, etc.) to make full use depending on your preferences.

-----

Some of the reasoning:

    - Analyses are rarely only run once even within the same project. Automating as much as possible saves time and errors. The setup can be costly initially but over time this pays off, particularly when needing to track errors, confirming results, handing over or reconstructing the history and reasoning (even to yourself months later).
    - Usually a project is built around one data set/experiment/question but even in this case it's easy to see potential gains from automating and packaging.
    - Packaging your project can help with reproducibility, freezing code, version control, collaboration and general mental sanity (while managing a project at least).
    - Later on the code or parts of it could be extracted to work on the general case as a separate entity.
    - This package is based on Python but the same applies to other languages. See discussions on writing your projects as packages in R (R. Flight_, H. Parker_ (also here_), H. Wickham_ and others_ for example). Hadley Wickham has a great ecosystem_ and a book_ on doing the same (and much more) with R_.
    
.. _Flight: http://rmflight.github.io/posts/2014/07/analyses_as_packages.html
    
.. _Parker: https://hilaryparker.com/2014/04/29/writing-an-r-package-from-scratch/

.. _here: https://hilaryparker.com/2013/04/03/personal-r-packages/

.. _Wickham: http://r-pkgs.had.co.nz/intro.html

.. _others: https://github.com/kbroman/broman


.. _book: http://r-pkgs.had.co.nz/

.. _ecosystem: http://hadley.nz/

.. _R: https://www.r-project.org/

-----

Other similar packages:

I discovered CookieCutter_ while working on this. It does what I have setup here better, with useful features, flexibility and many templates for different types of projects.

.. _CookieCutter: https://github.com/audreyr/cookiecutter-pypackage

Also see its data-science_ and reproducibility_ templates, they look good.

.. _reproducibility: https://github.com/mkrapp/cookiecutter-reproducible-science

.. _data-science: https://github.com/drivendata/cookiecutter-data-science


Installation
############

I've tested on MAC OS X and Linux. Untested in Windows and Python 2.7. 

Please raise an issue if you have problems.

Dependencies
============

- Python 3.5
- See requirements.rst for Python libraries needed
- None external


From GitHub
===========

To download and install from GitHub (you need git installed), at the command line do:

.. code-block:: bash

   pip install git+git://github.com/AntonioJBT/project_quickstart.git

or clone from GitHub (https example, you may need ssh):

.. code-block:: bash

   git clone https://github.com/AntonioJBT/project_quickstart.git
    
   cd project_quickstart

   python setup.py install

See stackoverflow_ example and pip docs_ for further help and explanations pip and git installs.

.. _stackoverflow: http://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github
.. _docs: https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support/pip_install.html#vcs-support


pip
===

.. code-block:: bash

   pip install project_quickstart

Conda
=====

TODO


Usage
#####

Create a project directory skeleton. From the command line do:

.. code-block:: bash

   project_quickstart --help

   project_quickstart -n my_super_project

   project_quickstart --script-R my_super_script # which will create an R script template called my_super_script.R

   project_quickstart --script-python my_super_script # which will create a Python script template called my_super_script.py

This will create data, code, manuscript and results directories along with Python and R template scripts and the necessary skeleton files for Python packaging, Docker, Travis CI, Sphinx, etc.

The --script options will create additional copies of script templates in the current working directory. 

Citation
########

If you use this package please cite it (!):

.. image:: https://zenodo.org/badge/79537885.svg
   :target: https://zenodo.org/badge/latestdoi/79537885
   

Contribute
##########

`Issue Tracker`_

.. _`Issue Tracker`: https://github.com/AntonioJBT/project_quickstart/issues

You are more than welcome to fork or submit pull requests (!).


Change log
##########

v0.2

- Initial release


License
#######

GPL-3


More details and suggestions
############################

Project workflow suggestions
============================

#. Run this package to setup folders, github repo structure, code testing, py package files, etc.
#. Download packages, tools, etc. Setup Docker, conda kaspel, or other form of tracking environment, packages and their versions.
#. Manually connect GitHub with integrated services (Travis CI, Zenodo, RTD).
#. Code and test code with tox, travis and py.test
#. Analyse, ...
#. Create new scripts, new pipelines, test them
#. Document code as you go, update with sphinx autodoc
#. Generate internal report with plots, text, etc.
#. Freeze with release tag + zenodo archiving and/or tar ball with py sdist
#. Repeat cycle

-----

General notes
=============

project_quickstart.py creates a folder structure with file templates for:

- data
- code
- results
- manuscript (reports, general documents, references, etc.)

See this layout_ for one explanation on organising Python projects

.. _layout: https://www.cgat.org/downloads/public/cgatpipelines/documentation/Reference.html#term-pipeline-scripts

project_quickstart.py copies the contents of project_quickstart/templates/project_template/ so as to have all the skeleton files needed for:

- Github repository files (but not .git) like: .gitignore, README, THANKS, TODO, LICENCE, etc.
- Travis testing files, tests dir with skeleton files
- Tox python testing
- Python packaging files
- Dockerfile
- etc
- Zenodo, see Zenodo_ GitHub guide. Allow permissions and then with each tag release Zenodo archives the repo and gives it a DOI. See also SSI blog_ on Zenodo.

These go into the code directory.

.. _Zenodo: https://guides.github.com/activities/citable-code/
	
.. _blog: https://www.software.ac.uk/blog/2016-09-26-making-code-citable-zenodo-and-github

Make additional script template copies with project_quickstart.py (located in project_quickstart/templates/project_template/).

-----

Testing
=======

- See tox, travis and py.test for a proper setup of py virtualenv, CI and unit testing respectively.
- Check travis setup, add pep8 and flake8 to improve your code.
- See CGAT docs for an explanation on testing_.
	
.. _testing: https://www.cgat.org/downloads/public/cgat/documentation/testing.html#testing

-----

Documentation
=============

After setting up a project, edit the INI and rst files so that variables that get repeated (such as project name, author, date, etc.) are automatically passed to the various files that need them (setup.py, Dockerfile, manuscript_template, etc.). These will get substituted when running python setup.py or rendering rst documents for instance.

Different renderers can give slightly different results (e.g. GitHub, RTD, Sphinx, rst2pdf, etc.)

rst2pdf can substitute rst variables but pandoc doesn't seem to do it properly.

See some notes in CGAT reports_.

.. _reports: https://www.cgat.org/downloads/public/cgatpipelines/documentation/PipelineReports.html#writingreports

- Add Python docs with rst, Sphinx_, quickstart_
- Check doctests_
- See this tutorial_ for Sphinx and general python packaging/workflow
- See also `Jeff Knupp's tutorial`_ and other `similar blogs`_ on Python packaging.

.. _tutorial: https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

.. _Sphinx: http://www.sphinx-doc.org/en/stable/

.. _quickstart: http://thomas-cokelaer.info/tutorials/sphinx/quickstart.html

.. _doctests: http://thomas-cokelaer.info/tutorials/sphinx/doctest.html

.. _`Jeff Knupp's tutorial`: https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

.. _`similar blogs`: https://www.pydanny.com/cookie-project-templates-made-easy.html


Try to follow Python style guides. See projects where these have been slightly adapted as an example (CGAT style_).

.. _style: https://www.cgat.org/downloads/public/cgat/documentation/styleguide.html#styleguide

-----

Computing environment and archiving
===================================

Use releases as code freezes. These can be pubilc, remote, local, private, etc.

See bioconda_, contributing a recipe_ and guidelines_ to help manage the project's dependencies and computational environment.

.. _bioconda: https://bioconda.github.io/index.html
	
.. _recipe: https://bioconda.github.io/contribute-a-recipe.html
	
.. _guidelines: https://bioconda.github.io/guidelines.html

If your code is useful to others, you can make it available with PyPI, create a Dockerfile and/or Conda recipe.

-----

.. note::
	
	Many links are tutorials I've come across, if you know of other good ones please share them.
	
	Make sure to check the official sites and follow their tutorials for each of the tools as a primary source however.
	
	Feel free to fork, raise issues and send pull requests.
	
