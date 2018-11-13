#!/usr/bin/env bash

###########################
# Some references to check:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
# http://jvns.ca/blog/2017/03/26/bash-quirks/
# Bash traps:
# http://aplawrence.com/Basics/trapping_errors.html
# https://stelfox.net/blog/2013/11/fail-fast-in-bash-scripts/
###########################


###########################
# Set bash script options

# exit when a command fails
set -o errexit

# exit if any pipe commands fail
set -o pipefail

# exit when your script tries to use undeclared variables
set -o nounset

# trace what gets executed
set -o xtrace

set -o errtrace
###########################

###########################
# Variables to substitute:
python_exec=$1 # you'll need pythonw if on a Mac
pandas_out=my_dataframe
infile=my_dataframe.tsv
plotA=my_dataframe_gender_glucose_boxplot.svg
plotB=my_dataframe_age_histogram.svg
svg_out=F1_my_dataframe
###########################

###########################
# First set of examples
${python_exec} ../code/pq_example/pq_example.py --createDF -O ${pandas_out}
Rscript ../code/pq_example/pq_example.R -I ${infile}
Rscript ../code/pq_example/plot_pq_example_pandas.R -I ${infile}
${python_exec} ../code/pq_example/svgutils_pq_example.py \
                        --plotA=${plotA} \
                        --plotB=${plotB} \
                        -O ${svg_out}
###########################

###########################
# Second set of examples
# Reset variables (it would be better to change names to avoid confusion):
plotA=mtcars_cyl_wt_boxplot_2.svg
plotB=mtcars_hp_qsec_scatterplot.svg
svg_out=F1_mtcars

Rscript ../code/pq_example/pq_example_mtcars.R
Rscript ../code/pq_example/plot_pq_example_mtcars.R
${python_exec} ../code/pq_example/svgutils_pq_example.py --plotA=${plotA} \
                                                 --plotB=${plotB} \
                                                 -O ${svg_out}
###########################

###########################
# Additional plotting
# Reset variables:
plotA=mtcars_wt_histogram.svg
plotB=mtcars_boxplot_lm.svg
svg_out=F2_mtcars

${python_exec} ../code/pq_example/svgutils_pq_example.py --plotA=${plotA} \
                                                 --plotB=${plotB} \
                                                 -O ${svg_out}
###########################

###########################
# Create the report:
cp -r ../code/pq_example/pipeline_pq_example/configuration .
cd configuration
make html
ln -fs _build/html/report_pipeline_pq_example.html .
make latexpdf
ln -fs _build/latex/pq_example.pdf .
#open pq_example.pdf report_pipeline_pq_example.html # on Mac
###########################
