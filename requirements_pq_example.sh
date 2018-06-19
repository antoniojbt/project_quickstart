#!/usr/bin/env bash
  
# Set bash script options:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
set -o errexit
set -o pipefail
set -o nounset

# You need to install conda first, then run:
# Create a virtual environment and install
# project_quickstart
# a fork of CGATPipelines
# cgat
# dependencies for project_quickstart's example

# Create conda environment:
bash -c 'conda create -yn pq_test python'
bash -c 'conda activate pq_test'

# Install project_quickstart and pq_example requirements:
bash -c 'wget https://raw.githubusercontent.com/AntonioJBT/project_quickstart/master/requirements.rst ; \
         pip install -r requirements.rst ; \
         pip install svgutils cairosvg ; \
         pip install --upgrade git+git://github.com/AntonioJBT/project_quickstart.git ; \
         pip install sphinxcontrib-bibtex ; \
         conda install -y r-docopt ; \
         conda install -y r-data.table'

# Get R packages not available with conda:
bash -c 'R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("stargazer", repos = "http://cran.us.r-project.org") ; library("stargazer")' ; \
         conda install -y r-ggplot2 ; \
         R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("svglite", repos = "http://cran.us.r-project.org") ; library("svglite")' ; \
         conda install -y r-string'

# Install CGAT tools with fork:
#bash -c 'wget https://raw.githubusercontent.com/AntonioJBT/CGATPipeline_core/master/requirements.txt ; \
#         pip install -r requirements.txt ; \
#         pip install git+git://github.com/AntonioJBT/CGATPipeline_core.git ; \
#         pip install cgat ; \
#         conda install -y rpy2'

# Finish and deactivate conda environment:
bash -c 'conda deactivate'
echo "All done, packages downloaded and installed. Activate your environment
using 'conda activate pq_test'"
