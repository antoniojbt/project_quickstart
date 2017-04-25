####
Plan 
####

:Date: 25 April 2017

Current state
#############

- B with T and E

- Wrap pipe quickstart


TO DO
#####

- Setup Tox properly
- Travis needs tests
- Correct pep8 and flake8 errors
- Conda recipe
- Zenodo hook
- Add Travis tests for R template
- Update external dependencies file, see some help here_. Consider using pyup.io for alerts on package updates?

.. _here: https://www.cgat.org/downloads/public/cgat/documentation/modules/Requirements.html

- Keep track of installations for Docker. Check conda kapsel_ and here_.

.. _kapsel: https://conda.io/docs/kapsel/

.. _here: https://github.com/conda/kapsel

- Add a project checklist template (eg with comp bio best practice checklist, conda recipe, zenodo deposit, etc.)
- Automatically run pipeline_quickstart.py at project creation?
- Add R's sessionInfo()
- Add Python and shell env equivalents to logs (pip freeze, conda list, etc.). See Experiment.py
- Add scan/ppt pipeline workflow plus notes
- Sphinx and docs, see here_ for a different solution.

.. _here: https://daler.github.io/sphinxdoc-test/includeme.html

- Have methods and plot scripts output legend\*.rst with parameters used, method\*.rst and generic interpretation\*.rst files output to disk to then glob into manuscript template.
