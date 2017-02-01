
'''
Usage:
    project_quickstart.py (--set-name=<start_procrastinating>) ...

to start a new project. 
This will create a new directory, subfolders and files in the current directory that will help quickstart your data science project.

    project_quickstart.py --set-name=<start_procrastinating>
    project_quickstart.py -f | --force
    project_quickstart.py -h | --help
    project_quickstart.py --version
    project_quickstart.py --quiet
    project_quickstart.py --verbose
    project_quickstart.py -L | --log <project_quickstart.log>
    
Options:
    -f --force     Careful! Creates a new project and overwrites anything with the same name
    -h --help     Show this screen.
    --version     Show version.
    --quiet      print less text
    --verbose    print more text
    -L --log     log file name. [default: project_quickstart.log]
'''
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    sys.exit(main())