# https://python-packaging.readthedocs.io/en/latest/minimal.html
# For a fuller example see: https://github.com/CGATOxford/UMI-tools/blob/master/setup.py
# Or: https://github.com/CGATOxford/cgat/blob/master/setup.py

# TO DO: update with further options such as include README.rst and others when ready

# TO DO: to add tests see https://python-packaging.readthedocs.io/en/latest/testing.html

# See also this example: https://github.com/pypa/sampleproject/blob/master/setup.py

# This may be a better way, based on Py3: http://www.diveintopython3.net/packaging.html

from distutils.core import setup
#from setuptools import setup # Py2

setup(name = 'project_quickstart',
      packages = ['project_quickstart'],
#      install_requires=[
#            'cgat',
#            'CGATPipelines',
#      ],
      version = '0.1',
      url = '',
      download_url = '',
      author = 'Antonio J Berlanga-Taylor',
      author_email = 'a.berlanga at imperial.ac.uk',
      license = 'GPL-3.0',
      zip_safe = False,
      classifiers = ["Programming Language :: Python",
                     "Programming Language :: Python :: 3",
                     "Development Status :: Alpha",
                     "Environment :: Other Environment",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                     "Operating System :: Linux and OSX",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                    ],
      description = 'Data science Python project quickstart',
      keywords = ['', ''],
      long_description = ''
     )
