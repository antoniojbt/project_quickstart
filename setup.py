#################

# https://python-packaging.readthedocs.io/en/latest/minimal.html
# For a fuller example see: https://github.com/CGATOxford/UMI-tools/blob/master/setup.py
# Or: https://github.com/CGATOxford/cgat/blob/master/setup.py

# TO DO: update with further options such as include README.rst and others when ready

# TO DO: to add tests see https://python-packaging.readthedocs.io/en/latest/testing.html

# See also this example: https://github.com/pypa/sampleproject/blob/master/setup.py

# This may be a better way, based on Py3: http://www.diveintopython3.net/packaging.html

# To package, check setup.py first:
# python setup.py check
# Then create a source distribution:
# python setup.py sdist
# which will create a dist/ directory and a compressed file inside with your package.
# For uploading to PyPi see http://www.diveintopython3.net/packaging.html#pypi

#################

from distutils.core import setup
#from setuptools import setup # Py2

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

CONFIG.read('project_quickstart.ini')
for key in CONFIG:
    print(key, CONFIG[key])
#################

#################
# Actual setup.py instructions:
setup(name = CONFIG['metadata']['project_name'], #'project_quickstart',
      packages = CONFIG['metadata']['project_name'],
#      install_requires=[
#            'cgat',
#            'CGATPipelines',
#      ],
      version = CONFIG['metadata']['prog_version'],
      url = CONFIG['metadata']['project_url'],
      download_url = CONFIG['metadata']['project_url'],
      author = CONFIG['metadata']['author_name'],
      author_email = CONFIG['metadata']['author_email'],
      license = CONFIG['metadata']['license'],
      classifiers = ["Programming Language :: Python", # see https://pypi.python.org/pypi?:action=list_classifiers
                     "Programming Language :: Python :: 3",
                     "Development Status :: 2- Pre-Alpha",
                     "Environment :: Other Environment",
                     "Intended Audience :: Science/Research",
                     "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                     "Operating System :: OS Independent",
                     "Topic :: Utilities",
                     "Topic :: Scientific/Engineering :: Bio-Informatics"
                    ],
      description = CONFIG['metadata']['project_short_description'],
      keywords = CONFIG['metadata']['keywords'],
      long_description = CONFIG['metadata']['long_description']
      )
#################
