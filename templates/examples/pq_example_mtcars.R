#!/usr/bin/env Rscript

######################
# R script to run with docopt for command line options:
'
pq_example_mtcars.R
===================

Author: |author_names| 
Release: |version|
Date: |today|


Purpose
=======

|description|

Runs some basic stats and plots as examples using the mt_cars dataset available in R.


Usage and options
=================

These are based on docopt_ for R:

https://github.com/docopt/docopt.R
https://cran.r-project.org/web/packages/docopt/index.html

To run, type:
    Rscript pq_example_mtcars.R [options]

Usage: pq_example_mtcars.R [--session=<R_SESSION_NAME>]
       pq_example_mtcars.R [-h | --help]

Options:
  --session=<R_SESSION_NAME>      R session name if to be saved
  -h --help                       Show this screen

Input:

    None needed, the script loads the data "mtcars"

Output:

    A boxplot and scatterplot from the R dataset mtcars as svg files
    and an html table of a linear regression output.

Requirements:

    library(docopt)
    library(stargazer)

Documentation
=============

    For more information see:

    |url|
' -> doc

# Load docopt:
library(docopt, quietly = TRUE)
# Retrieve the command-line arguments:
args <- docopt(doc)
# See:
# https://cran.r-project.org/web/packages/docopt/docopt.pdf
# docopt(doc, args = commandArgs(TRUE), name = NULL, help = TRUE,
# version = NULL, strict = FALSE, strip_names = !strict,
# quoted_args = !strict)

# Print to screen:
str(args)
# Within the script specify options as:
# args[['--session']]
# args $ `-I` == TRUE
######################

######################
# Logging
# This can be taken care of by CGAT Experiment.py if running as a pipeline.
# Otherwise there seem to be few good alternatives. A workaround is this code:
# logging.R
# In the script_templates dir of project_quickstart.
# It does not run on it own though, needs copy/pasting for now.
######################

######################
# Load a previous R session, data and objects:
#load('R_session_saved_image_order_and_match.RData', verbose=T)
######################

######################
# Import libraries
# source('http://bioconductor.org/biocLite.R')
suppressMessages(library(stargazer, quietly = TRUE)) # tables for linear regressions
######################


######################
# Load dataset:
input_name <- 'mtcars'
data('mtcars')
input_data <- as.data.frame(mtcars)

# Explore data:
class(input_data)
dim(input_data) # nrow(), ncol()
str(input_data)
head(input_data)
tail(input_data)
colnames(input_data)
###################### 

###################### 
# Do some stats, simple examples here:
# What's the question? What's the hypothesis?
# Descriptive:
nrow(input_data)
length(which(complete.cases(input_data) == TRUE))
summary(input_data)
summary(input_data[, c('wt', 'qsec', 'gear')])
# Process variables:
cyl_factor <- factor(input_data$cyl)
cyl_factor
gear_factor <- factor(input_data$gear)
gear_factor

# Some basic exploratory plots
# Plot here or use a separate plot_template.R script (preferable if processing
# large datasets, process first, save, plot separately):
plot_name <- svg(sprintf('%s_boxplot_lm.svg', input_name))
boxplot(input_data$mpg ~ cyl_factor)
dev.off()

plot_name <- svg(sprintf('%s_scatterplot_lm.svg', input_name))
plot(input_data$qsec ~ cyl_factor)
dev.off()

# Inferential:
pass_formula <- 'qsec ~ cyl_factor + hp + wt + gear_factor'
lm_input_data <- lm(formula = pass_formula, data = input_data)
summary(lm_input_data)
stargazer(out = sprintf('%s_lm_table.html', input_name), 
          style = 'all',
          lm_input_data,
          summary = TRUE,
          title = 'Car speed adjusted for cylinders, horse power, weight and gears'
          )

stargazer(out = sprintf('%s_lm_table.tex', input_name), 
          style = 'all',
          lm_input_data,
          summary = TRUE,
          title = 'Car speed adjusted for cylinders, horse power, weight and gears'
          )
######################


######################
## Save some text:
# cat(file <- output_file, some_var, '\t', another_var, '\n', append = TRUE)
######################


######################
# The end:
# Remove objects that are not necessary to save:
# ls()
# object_sizes <- sapply(ls(), function(x) object.size(get(x)))
# as.matrix(rev(sort(object_sizes))[1:10])
#rm(list=ls(xxx))
#objects_to_save <- (c('xxx_var'))
#save(list=objects_to_save, file=R_session_saved_image, compress='gzip')

# Filename to save current R session, data and objects at the end:
if (is.null(args[['--session']]) == FALSE) {
  save_session <- as.character(args[['--session']]) #args $ `--session`
  R_session_saved_image <- sprintf('R_session_saved_image_%s.RData', save_session)
  print(sprintf('Saving an R session image as: %s', R_session_saved_image))
  save.image(file = R_session_saved_image, compress = 'gzip')
} else {
  print('Not saving an R session image, this is the default. Specify the --session option otherwise')
}

# If using Rscript and creating plots, Rscript will create the file Rplots.pdf 
# by default, it doesn't look like there is an easy way to suppress it, so deleting here:
print('Deleting the file Rplots.pdf...')
system('rm -f Rplots.pdf')
sessionInfo()
q()

# Next: run the script for xxx
######################
