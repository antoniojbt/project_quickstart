.. image:: https://travis-ci.org/AntonioJBT/project_quickstart.svg?branch=master
   :target: https://travis-ci.org/AntonioJBT/project_quickstart

.. image:: https://readthedocs.org/projects/project-quickstart/badge/?version=latest
   :target: http://project-quickstart.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


##################
Project Quickstart
##################

..
    A description of your project
    Links to the project's ReadTheDocs page
    A TravisCI button showing the state of the build
    "Quickstart" documentation (how to quickly install and use your project)
    A list of non-Python dependencies (if any) and how to install them

.. See example: http://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1

..
   $project
   ========

   $project will solve your problem of where to start with documentation,
   by providing a basic explanation of how to do it easily.

   Look how easy it is to use:

    import project
    # Get your stuff done
    project.do_stuff()

   Features
   --------

   - Be awesome
   - Make things faster

   Installation
   ------------

   Install $project by running:

    install project

   Contribute
   ----------

   - Issue Tracker: github.com/$project/$project/issues
   - Source Code: github.com/$project/$project

   Support
   -------

   If you are having issues, please let us know.
   We have a mailing list located at: project@google-groups.com

   License
   -------

   The project is licensed under the BSD license.


In progress...

Boilerplate tools and templates for setting up a data analysis project. The package is setup with: 

- reproducibility concepts in mind
- Ruffus_ as a pipeline tool and CGAT_ tools for support 
- Python_ programming and packaging_
- restructuredText_ and Sphinx_ for reporting
- Travis_ and tox_ for testing
- Conda_ and Docker_ for management and development
- GitHub_ for version control

I've additionally put some basic instructions/reminders to link GitHub with:

- ReadtheDocs_
- Zenodo_ (for archiving your code and generating a DOI)
- Travis CI.

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

-----

Some of the reasoning:

    - Analyses are rarely only run once even within the same project. Automating as much as possible saves time and errors. The setup can be costly initially but over time this pays off, particularly when needing to track errors, confirming results, handing over or reconstructing the history and reasoning (even to yourself months later).
    - Usually a project is built around one data set/experiment/question but even in this case it's easy to see potential gains from automating and packaging.
    - Packaging your project can help with reproducibility, freezing code, version control, collaboration and general mental sanity (while managing a project at least).
    - Later on the code or parts of it could be extracted to work on the general case as a separate entity.
    - This package is based on Python but the same applies to other languages. See much more eloquent and deeper discussions on writing your projects as packages from R. Flight_, H. Parker_ (also here_), H. Wickham_ and others_ for example. Hadley Wickham has a great ecosystem_ and a book_ on doing the same (and much more) with R_.
    
.. _Flight: http://rmflight.github.io/posts/2014/07/analyses_as_packages.html
    
.. _Parker: https://hilaryparker.com/2014/04/29/writing-an-r-package-from-scratch/

.. _here: https://hilaryparker.com/2013/04/03/personal-r-packages/

.. _Wickham: http://r-pkgs.had.co.nz/intro.html

.. _others: https://github.com/kbroman/broman

.. _book: http://r-pkgs.had.co.nz/

.. _ecosystem: http://hadley.nz/

.. _R: https://www.r-project.org/

-----

I discovered CookieCutter_ while working on this. It does what I have setup here better, with useful features, flexibility and many templates for different types of projects.

.. _CookieCutter: https://github.com/audreyr/cookiecutter-pypackage

Also see its data-science_ and reproducibility_ templates, they look good.

.. _reproducibility: https://github.com/mkrapp/cookiecutter-reproducible-science

.. _data-science: https://github.com/drivendata/cookiecutter-data-science

-----

To install:

TODO

From GitHub
===========

To download and install from GitHub (you need git installed), at the command line do::

|    project_quickstart
|    ├── project_quickstart
|    │   ├── __init__.py
|    │   └── scripts and other files
|    └── setup.py

.. code-block::

    $ pip install git+git://github.com/AntonioJBT/project_quickstart.git

..    $ pip install git+git://github.com/myuser/foo.git@v123
    or
    $ pip install git+git://github.com/myuser/foo.git@newbranch

or clone from GitHub (https example, you may need ssh)::

.. code-block::

    git clone https://github.com/AntonioJBT/project_quickstart.git
    
    python setup.py install


See stackoverflow_ example and pip docs_ for further help and explanations pip and git installs.

.. _stackoverflow: http://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github
.. _docs: https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support/pip_install.html#vcs-support


pip
===

TODO

Conda
=====

TODO


Usage
=====
TODO

.. code-block::
    
    project_quickstart.py --help


