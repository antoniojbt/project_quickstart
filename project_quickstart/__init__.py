import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def getDir(path):
    ''' Search path for the 'xxxx' directory for copying within cwd '''
    return os.path.join(_ROOT, 'data', path)
    return os.path.join(_ROOT, f'project_quickstart-{prog_version}', path)

#print(getDir('templates'))
