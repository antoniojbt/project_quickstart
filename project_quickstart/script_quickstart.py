'''project_quickstart.py - setup a new python based project
===========================================================

:Author: Antonio Berlanga-Taylor
:Release: $Id$
:Date: |today|

Purpose
-------
This script creates a python project template.

It is mostly taken from CGAT's
https://github.com/CGATOxford/CGATPipelines/blob/master/scripts/pipeline_quickstart.py


Options
=======

Usage: project_quickstart.py --set-name=start_procrastinating

To start a new project

This will create a new directory, subfolders and files in the current directory

that will help quickstart your data science project.

-h --help    show this
--quiet      print less text
--verbose    print more text
-L --log     log file name.

Documentation
-------------

.. todo::

  Add docs
  Add tree structure

Code
----

'''

import sys
import re
import os
import shutil
#import CGAT.Experiment as E
from docopt import docopt


##############################
def main(argv=sys.argv):

    parser = E.OptionParser(version="%prog version: $Id$",
                            usage=globals()["__doc__"])

    parser.add_option("-d", "--dest", dest="destination", type="string",
                      help="destination directory.")

    parser.add_option(
        "-n", "--set-name", dest="name", type="string",
        help="name of this project. 'project_' will be prefixed.")

    parser.add_option(
        "-f", "--force-output", dest="force", action="store_true",
        help="overwrite existing files.")

    parser.set_defaults(
        destination=".",
        name=None,
        force=False,
    )

    (options, args) = E.Start(parser)

    if not options.name:
        raise ValueError("please provide a project name")

##############################

#    reportdir = os.path.abspath("code/pipeline_docs/pipeline_%s" % options.name)
    confdir = os.path.abspath("code/project_%s" % (options.name))

    destination_dir = options.destination

##############################

    # create directories
    for d in ("", "code", "data",
              "data/raw",
              "data/processed",
              "data/external",
              "results_1",
              "manuscript"):

        dd = os.path.join(destination_dir, d)
        if not os.path.exists(dd):
            os.makedirs(dd)

##############################

    # copy files
    # replaces all instances of template with options.name within
    # filenames and inside files.
    rx_file = re.compile("template")
    rx_template = re.compile("@template@")

    srcdir = P.CGATPIPELINES_PIPELINE_DIR

##############################

    def copy(src, dst, name):

        # remove "template" and the pipeline type from file/directory
        # names.
        fn_dest = os.path.join(
            destination_dir,
            dst,
            rx_type.sub("", rx_file.sub(name, src)))

        fn_src = os.path.join(srcdir,
                              "pipeline_template_data", src)

        E.debug("fn_src=%s, fn_dest=%s, src=%s, dest=%s" %
                (fn_src, fn_dest, src, dst))

        if os.path.exists(fn_dest) and not options.force:
            raise OSError(
                "file %s already exists - not overwriting." % fn_dest)

        outfile = open(fn_dest, "w")
        infile = open(fn_src)
        for line in infile:
            outfile.write(rx_reportdir.sub(reportdir,
                                           rx_template.sub(name, line)))

        outfile.close()
        infile.close()

##############################

    def copytree(src, dst, name):

        fn_dest = os.path.join(destination_dir, dst, rx_file.sub(name, src))
        fn_src = os.path.join(srcdir, "pipeline_template_data", src)

        if os.path.exists(fn_dest) and not options.force:
            raise OSError(
                "file %s already exists - not overwriting." % fn_dest)

        shutil.copytree(fn_src, fn_dest)

    for f in ("conf.py",
              "pipeline.ini"):
        copy(f, 'src/pipeline_%s' % options.name, name=options.name)

##############################

    # copy the script
    copy("pipeline_template_%s.py" % options.pipeline_type, 'src',
         name=options.name)

##############################

    # create links
    for src, dest in (("conf.py", "conf.py"),
                      ("pipeline.ini", "pipeline.ini")):
        d = os.path.join("report", dest)
        if os.path.exists(d) and options.force:
            os.unlink(d)
        os.symlink(os.path.join(confdir, src), d)

    for f in ("cgat_logo.png",):
        copy(f, "%s/_templates" % reportdir,
             name=options.name)

    for f in ("themes",):
        copytree(f, "src/pipeline_docs",
                 name=options.name)

    for f in ("contents.rst",
              "pipeline.rst",
              "__init__.py"):
        copy(f, reportdir,
             name=options.name)

    for f in ("Dummy.rst",
              "Methods.rst"):
        copy(f, "%s/pipeline" % reportdir,
             name=options.name)

    for f in ("TemplateReport.py", ):
        copy(f, "%s/trackers" % reportdir,
             name=options.name)

    absdest = os.path.abspath(destination_dir)

    name = options.name

##############################

    print(""" Time to start procrastinating! Welcome to your %(name)s project. 
    
    The folder structure and files have been successfully copied to `%(destination_dir)s`. 
    Files have been copied 'as is'. You can edit the configuration file and run:
    
    python project quickstart.py --update
    
    to update files with your chosen parameters (note files get overwritten!).
    
    The folder structure is %(tree_dir)s.
    Feel free to raise issues, fork or contribute at:
    
    https://github.com/AntonioJBT/project_quickstart
    
    Have fun!
    """ % locals()
         )

    E.Stop()

##############################

if __name__ == "__main__":
   sys.exit(main())
