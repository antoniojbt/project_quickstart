#!/usr/bin/env bash
  
# Set bash script options:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
set -o errexit
set -o pipefail
set -o nounset

# You need to install conda first, then run:
# Create a virtual environment:
conda create -yn py35_test python=3.5
/bin/bash -c 'source activate py35_test'

# Install project_quickstart (if you don't have it already):
wget https://raw.githubusercontent.com/AntonioJBT/project_quickstart/master/requirements.rst
pip install -r requirements.rst 
pip install project_quickstart

# Install a fork of CGATPipelines:
wget https://raw.githubusercontent.com/AntonioJBT/CGATPipeline_core/master/requirements.txt
pip install -r requirements.txt
pip install git+git://github.com/AntonioJBT/CGATPipeline_core.git

# Install cgat:
pip install cgat

# Install dependencies for project_quickstart's example:
pip install sphinxcontrib-bibtex
conda install -y rpy2
conda install -y r-docopt
conda install -y r-data.table
R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("stargazer", repos = "http://cran.us.r-project.org") ; library("stargazer")'
conda install -y r-ggplot2
R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("svglite", repos = "http://cran.us.r-project.org") ; library("svglite")'

# Then activate the environment in your terminal:
# source activate py35_test
