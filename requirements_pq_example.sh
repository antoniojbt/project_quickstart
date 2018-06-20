#!/usr/bin/env bash

echo "
This script is intended as an example only.
If you get errors simply copy-paste commands and adapt to
the system you are working on.
"

# Set bash script options:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
# Exit when a command fails:
set -o errexit
# Catch  piped commands which fail. The exit status of
# the last command that threw a non-zero exit code is returned:
set -o pipefail
# Exit when trying to use an undeclared variable:
set -o nounset

# You need to install conda first, then run:

# Create conda environment:
conda create -yn pq_test python
conda activate pq_test

# Specify conda channels to avoid clashes with R:
conda config --add channels conda-forge
conda config --add channels bioconda

# Install R:
conda install -y r

# Install project_quickstart and pq_example requirements:
bash -c 'wget https://raw.githubusercontent.com/AntonioJBT/project_quickstart/master/requirements.rst ; \
         pip install -r requirements.rst ; \
         pip install svgutils cairosvg ; \
         pip install --upgrade git+git://github.com/AntonioJBT/project_quickstart.git ; \
         pip install sphinxcontrib-bibtex ; \
         conda install -y r-docopt r-data.table r-ggplot2 r-stringr; \
         conda install pandas matplotlib scipy'

# Get R packages not available with conda (in the channels specified, might be
# elsewhere):
R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("stargazer", repos = "http://cran.us.r-project.org") ; library("stargazer")'
R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("svglite", repos = "http://cran.us.r-project.org") ; library("svglite")'

# Install CGAT tools with fork:
#bash -c 'wget https://raw.githubusercontent.com/AntonioJBT/CGATPipeline_core/master/requirements.txt ; \
#         pip install -r requirements.txt ; \
#         pip install git+git://github.com/AntonioJBT/CGATPipeline_core.git ; \
#         pip install cgat ; \
#         conda install -y rpy2'

# Use cgat-core and cgat-flow:
#bash -c 'wget https://raw.githubusercontent.com/cgat-developers/cgat-core/master/conda_requires.txt ; \
#         pip install -r conda_requires.txt ; \
#         pip install --upgrade git+git://github.com/cgat-developers/cgat-core'

# Finish and deactivate conda environment:
conda deactivate
echo "All done, packages downloaded and installed. Activate your environment
using 'conda activate pq_test'"
