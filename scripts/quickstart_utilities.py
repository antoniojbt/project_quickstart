'''
Utilities for project_quickstart.py

:Author: Antonio J Berlanga-Taylor
:Date:


Boilerplate tools for quickstarting a data analysis project:

https://github.com/AntonioJBT/project_quickstart

'''

# Load arguments from an INI file
# See as an example:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py

def load_ini_config():
    try:  # Python 2
        from ConfigParser import ConfigParser
        from StringIO import StringIO
    except ImportError:  # Python 3
        from configparser import ConfigParser
        from io import StringIO

    import sys
    import os
    import glob

    # By using `allow_no_value=True` we are allowed to
    # write `--force` instead of `--force=true` below.
    config = ConfigParser(allow_no_value=True)

    # Load the INI file:
    if glob.glob('*.ini'):
        INI_file = glob.glob('*.ini')
    else:
        print('No configuration (e.g. xxx.ini) file present in the directory')
        sys.exit()

    # ConfigParser requires a file-like object and
    # no leading whitespace.
    config_file = StringIO('\n'.join(INI_file.split()))
    config.readfp(config_file)

    # ConfigParsers sets keys which have no value
    # (like `--force` above) to `None`. Thus we
    # need to substitute all `None` with `True`.
    return dict((key, True if value is None else value)
                for key, value in config.items('default-arguments'))


    ini_config = load_ini_config()

    # Arguments take priority over INI, INI takes priority over JSON:
    result = arguments, ini_config

    from pprint import pprint
    print('\nINI config:')
    pprint(ini_config)
    print('\nResult:')
pprint(result)


