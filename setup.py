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
#from distutils.core import setup
#from setuptools import setup # Py2
from setuptools.command.install import install
from setuptools import setup, find_packages
import sys

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
# Print kyes (sections):
print('Values for setup.py:', '\n')
for key in CONFIG:
    for value in CONFIG[key]:
        print(key, value, '\n', CONFIG[key][value])
#################


#################
# Get version:
sys.path.insert(0, CONFIG['metadata']['project_name'])
import version

version = version.__version__
#################


#################
# Get info from README and version.py:
# Get Ptyhon modules required:
install_requires = []

with open('requirements.rst') as required:
    for line in (required):
        if not line.startswith('#') and not line.startswith('\n'):
            line = line.strip()
            install_requires.append(line)

#print(install_requires)

with open('README.rst', 'rt') as readme:
    description = readme.read()


# Give warning:
class CustomInstall(install):
    def initialize_options(self):
        if sys.version < '3':
            print(CONFIG['metadata']['project_name'], " requires Python 3.6 or higher.")
            sys.exit(1)

        return install.initialize_options(self)
#################


#################
# Actual setup.py instructions:
setup(name = CONFIG['metadata']['project_name'],
      packages = [CONFIG['metadata']['packages_setup']], # needs to be passed
                                                         # as list
      install_requires = install_requires,
      version = CONFIG['metadata']['prog_version'],
      url = CONFIG['metadata']['project_url'],
      download_url = CONFIG['metadata']['download_url'],
      author = CONFIG['metadata']['author_name'],
      author_email = CONFIG['metadata']['author_email'],
      license = CONFIG['metadata']['license'],
#      classifiers = [CONFIG['metadata']['classifiers_setup']], 
       # needs to be passed as list
       # gives many errors when registering manually in pip
      description = CONFIG['metadata']['project_short_description'],
      keywords = CONFIG['metadata']['keywords'],
      #long_description = CONFIG['metadata']['long_description'],
      long_description = description,
      include_package_data = True,
      entry_points={
          'console_scripts': [
              'project_quickstart.py = project_quickstart.py:main',
              ]},
      cmdclass = {'install': CustomInstall}
          )
#################
