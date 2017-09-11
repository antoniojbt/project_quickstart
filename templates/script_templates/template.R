######################
# R script to run with docopt for command line options:
'
script_name
===============

Author: |author_names| 
Release: |version|
Date: |today|


Purpose
=======

|description|

Runs some basic stats and plots as examples.

Usage and options
=================

These are based on docopt_ for R:

https://github.com/docopt/docopt.R
https://cran.r-project.org/web/packages/docopt/index.html

To run, type:
    Rscript script_name -I <INPUT_FILE> [options]

Usage: script_name (-I <INPUT_FILE>) [--session=<R_SESSION_NAME>]
       script_name [-h | --help]

Options:
  -I <INPUT_FILE>                 Input file name
  --session=<R_SESSION_NAME>      R session name if to be saved
  -h --help                       Show this screen

Input:

    A tab separated file with headers. This is read with data.table and stringsAsFactors = FALSE

Output:

    A boxplot and scatterplot from the R dataset mtcars as svg files and an html table of a linear regression output.

Requirements:

    library(docopt)
    library(data.table)
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
library(data.table)
library(stargazer) # tables for linear regressions
######################


######################
# Read files:
if (is.null(args[['-I']]) == FALSE) {
  input_name <- as.character(args[['-I']])#(args $ `-I`)
  # input_name <- as.character('mtcars')
  # input_data <- fread(input_name, sep = '\t', header = TRUE, stringsAsFactors = FALSE)
} else {
  # Stop if arguments not given:
  print('You need to provide an input file. This has to be tab separated with headers.')
  stopifnot(!is.null(args[['-I']]) == TRUE)
}
input_name

# Or load the example data:
data("mtcars")
input_data <- data.frame(mtcars)

# Explore data:
class(input_data)
dim(input_data)
head(input_data)
tail(input_data)
str(input_data)
colnames(input_data)
rownames(input_data)
###################### 

###################### 
# Do some stats, simple examples here:
# What's the question? What's the hypothesis?
# Descriptive:
class(input_data)
str(input_data)
complete.cases(input_data)
summary(input_data)
summary(input_data$gear)
summary(input_data$qsec)
cor(input_data$mpg, input_data$qsec)

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
          type = 'html',
          summary = TRUE,
          title = 'Car speed adjusted for cylinders, horse power, weight and gears'
          )
######################


######################
## Save some text:
cat(file <- output_file, some_var, '\t', another_var, '\n', append = TRUE)
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
