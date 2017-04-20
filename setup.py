import sys
import os
import glob

from ez_setup import use_setuptools
use_setuptools("10.0")
import setuptools

from setuptools import setup, find_packages, Extension

from distutils.version import LooseVersion
if LooseVersion(setuptools.__version__) < LooseVersion('1.1'):
    print ("Version detected:", LooseVersion(setuptools.__version__))
    raise ImportError(
        "Setuptools 1.1 or higher is required")

########################################################################
########################################################################
# collect umi_tools version
sys.path.insert(0, "project_quickstart")
import version

version = version.__version__

###############################################################
###############################################################
# Define dependencies 
# Perform a umi_tools Installation

major, minor1, minor2, s, tmp = sys.version_info

if (major == 2 and minor1 < 7) or major < 2:
    raise SystemExit("""project_quickstart requires Python 2.7 or later.""")

project_quickstart_packages = ["project_quickstart"]
project_quickstart_package_dirs = {'project_quickstart': 'project_quickstart'}

# debugging pip installation
#install_requires = []
#for requirement in (
#        l.strip() for l in open('requirements.txt') if not l.startswith("#")):
#    install_requires.append(requirement)

install_requires = [
#    "setuptools>=1.1",
#    "cython>=0.19",
#    "numpy>=1.7",
#    "pandas>=0.12.0",
    "future",
    "six",
    "docopt"]

# This is a hack. When Pysam is installed from source, the recorded
# version is 0.2.3, even though a more recent version is actaully
# installed. In the following, if pysam is not detected, pysam will be
# install, presumably this will be the lastest version. If pysam is
# present detect its version with pysam.__version__.  The only problem
# with this is that if pysam is present, but out of date, the system
# will not recognise the update

#try:
#    import pysam
#    if LooseVersion(pysam.__version__) < LooseVersion('0.8.4'):
#        print("""
#        
    ######################################################################
    #
    # WARNING:
    # Pysam is installed, but not recent enough. We will update pysam, but
    # the system may fail to detect that pysam has been updated. If this
    # happens please run setup again"
    #
    ######################################################################
#        """)

#        install_requires.append("pysam>=0.8.4")

#except ImportError:
#    install_requires.append("pysam")

##########################################################
##########################################################
# Classifiers
classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

setup(
    # package information
    name='project_quickstart',
    version=version,
    description='Boilerplate tools to quickly create a data science project skeleton',
    author='Antonio J Berlanga Taylor',
    author_email='i.sudbery@sheffield.ac.uk',
    license="GPL-3",
    platforms=["any"],
    keywords="computational genomics",
    long_description='project_quickstart',
    classifiers=list(filter(None, classifiers.split("\n"))),
    url="https://github.com/AntonioJBT/project_quickstart",
    download_url="https://github.com/AntonioJBT/project_quickstart",
    # package contents
    packages=project_quickstart_packages,
    package_dir=project_quickstart_package_dirs,
    include_package_data=True,
    # dependencies
    #setup_requires=['cython'],
    install_requires=install_requires,
    # extension modules
    # ext_modules=cythonize("umi_tools/_dedup_umi.pyx"),
    entry_points={
        'console_scripts': ['project_quickstart = project_quickstart.project_quickstart:main']
    },
    # other options
    zip_safe=False,
)
