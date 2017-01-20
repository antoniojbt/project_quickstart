'''
xxx.py - for xxx
================

See examples from cgat umi, etc, eg
https://github.com/CGATOxford/UMI-tools/blob/master/umi_tools/dedup.py

:Author: 
:Release: $Id$
:Date: |today|
:Tags: Computational pipelines

Purpose
=======

Methods
=======

Usage
=====

To use type::

    xxx.py [options] [arguments]

    xxx.py --help

Options
=======

-I    input file name.
-S    output file name.
-L    log file name.

'''
##############
import os
import sys
import glob
import imp

import pandas as pd
import numpy as np

# required to make iteritems python2 and python3 compatible
from builtins import dict

try:
    import CGAT.IOTools as IOTools
    import CGATPipeline.Pipeline as P
    import CGATPipeline.Experiment as E

except:
    import x as X

##############


def main(argv=None):

    argv = sys.argv

    path = os.path.abspath(os.path.dirname(__file__))

    if len(argv) == 1 or argv[1] == "--help" or argv[1] == "-h":
        print(globals()["__doc__"])

        return

    command = argv[1]

    (file, pathname, description) = imp.find_module(command, [path, ])
    module = imp.load_module(command, file, pathname, description)
    # remove 'umi-tools' from sys.argv
    del sys.argv[0]
    module.main(sys.argv)

if __name__ == "__main__":
sys.exit(main())
