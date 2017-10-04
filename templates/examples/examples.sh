#!/usr/bin/env bash

# Set bash script options:
# https://kvz.io/blog/2013/11/21/bash-best-practices/
set -o errexit
set -o pipefail
set -o nounset


# Variables to substitute:
pandas_out=my_dataframe
infile=my_dataframe.tsv
plotA=my_dataframe_gender_glucose_boxplot.svg
plotB=my_dataframe_age_histogram.svg
svg_out=F1_mydataframe

# First set of examples
pythonw ../code/pq_example/pq_example.py --createDF -O ${pandas_out}
Rscript ../code/pq_example/pq_example.R -I ${infile}
Rscript ../code/pq_example/plot_pq_example_pandas.R -I ${infile}
python ../code/pq_example/svgutils_pq_example.py \
                        --plotA=${plotA} \
                        --plotB=${plotB} \
                        -O ${svg_out}

# Second set of examples
# Reset variables, could change names to avoid confusion:
plotA=mtcars_cyl_wt_boxplot_2.svg
plotB=mtcars_hp_qsec_scatterplot.svg
svg_out=F1_mtcars

Rscript ../code/pq_example/pq_example_mtcars.R
Rscript ../code/pq_example/plot_pq_example_mtcars.R
python ../code/pq_example/svgutils_pq_example.py --plotA=${plotA} \
                                                 --plotB=${plotB} \
                                                 -O ${svg_out}

# Additional plotting
# Reset variables, could change names to avoid confusion:
plotA=mtcars_wt_histogram.svg
plotB=mtcars_boxplot_lm.svg
svg_out=F2_mtcars

python ../code/pq_example/svgutils_pq_example.py --plotA=${plotA} \
                                                 --plotB=${plotB} \
                                                 -O ${svg_out}

# Create the report:
cp -r ../code/pq_example/pipeline_pq_example/configuration_pipeline_pq_example .
cd configuration_pipeline_pq_example
make html
ln -fs _build/html/report_pipeline_pq_example.html .
make latexpdf
ln -fs _build/latex/pq_example.pdf .
open pq_example.pdf report_pipeline_pq_example.html # on Mac