from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
# Probably good to use MAJOR.MINOR.PATCH ?

#    MAJOR version (when you make incompatible API changes), or something arbitrarily import?
#    MINOR version when you add functionality in a backwards-compatible manner, and
#    PATCH version when you make backwards-compatible bug fixes.

# http://semver.org/


# Set up calling parameters from INI file:
# Modules with Py2 to 3 conflicts
from future import standard_library
standard_library.install_aliases()

#try:
#    import configparser
#except ImportError:  # Py2 to Py3
#    import Configparser as configparser

# Global variable for configuration file ('.ini')
#CONFIG = configparser.ConfigParser(allow_no_value = True)

#CONFIG.read('project_quickstart.ini')

#__version__ = CONFIG['metadata']['version']
__version__ = '0.2.3'

#print(CONFIG['metadata']['project_name'], 'version', __version__)
