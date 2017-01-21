################################
Plan 
################################

:Date: 20 January 2017
:Author: Antonio B 

Current state:
##############

- The plan is to create xxxx that can be automated using Ruffus and CGAT tools. 

- CGAT, ruffus, drmaa 

- There is a pipeline in progress in the src folder with a dummy report in the report folder (based on CGAT's quickstart pipeline).

- B with T and E

- Wrap pipe quickstart, add R quickstart, report quickstart, standard folder structure, instructions for dependencies, CLI runs, etc

Future work:
############


TO DO main tasks:
#################

- project_quickstart/scripts/project_quickstart.py basically just copies the contents of project_quickstart/templates/python_packaging.dir/
- project_quickstart/scripts/script_quickstart.py copies project_quickstart/templates/python_script_template.py
- project_quickstart/scripts/R_script_quickstart.R copies project_quickstart/templates/R_script_template.R
- project_quickstart/scripts/folder_structure.py creates a folder structure for a data science project:
	+ data
	+ code
	+ results
	+ manuscripts
	
- Pass variables such as project name, author, date, etc. automatically to the various files that need them (setup.py, Dockerfile, ?)
- Check travis setup, is pep8 running? flake8 gives errors and log at travis
- Update external dependencies file
- Keep track of installations for Docker, David has an initial dockerfile

PIPELINE PLAN
#############

.. todo::
	TO DO: scan/ppt pipeline workflow plus notes

-----


The output should be input for:


References
##########

Also see:
