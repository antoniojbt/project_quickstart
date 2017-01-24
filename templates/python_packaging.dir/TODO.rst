################################
Plan 
################################

:Date: 
:Author: 

Current state:
##############

-
-
-


Future work:
############


TO DO main tasks:
#################

Plan:

- What's the question?!
- Write project pipeline steps, scripts needed, pseudocode and sketch
- Write scripts, write it up as a package
- Check Travis setup: pep8, flake8, create unit tests
- Update python and external dependencies file

-----

To do manually:

- Upload to GitHub account
- Manually connect to Travis for testing, add image to README.rst
- Keep track of installations for Docker instructions
- Manually connect to Zenodo, each release will trigger an archive and DOI
- Manually connect to ReadtheDocs, triggers will build the package's documentation on their webpage:
	+ Manual configuration is needed on both the GitHub and ReadtheDocs sides:
		* Sign up to RTD, connect it to your GitHub account and allow permissions
		* At RTD setup the configuration as needed, check:
			
			Repo: https://github.com/github_username/project_name.git ;  Add the *.git* to it.
			Use virtualenv: (checked)
			Requirements file: requirements.txt
			The rest should be OK with the defualts. The EPUB option may need further configuring though.
			Copy the RTD image to your README.rst so the badge shows up.
		
- Setup conda recipe or PyPi if appropriate. See CookieCutter's helpful tutorial for PyPi_ instructions for example.

.. _Pypi: https://cookiecutter-pypackage.readthedocs.io/en/latest/pypi_release_checklist.html


PIPELINE PLAN
#############

.. todo::
	TO DO: 

-----


The output should be input for:


References
##########


Also see:

