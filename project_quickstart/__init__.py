'''
# Get locations of source code
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
    # __init__.py has the getDir() function
# MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation
'''

import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def getDir(path):
    ''' Get the absolute path for the package directory '''
    return os.path.join(_ROOT, 'data', path)
    return os.path.join(_ROOT, f'project_quickstart-{prog_version}', path)

#print(getDir('templates'))
