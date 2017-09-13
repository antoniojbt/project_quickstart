######################
# R script to run with docopt for command line options:
'
plot_template.R
===============

Author: |author_names| 
Release: |version|
Date: |today|


Purpose
=======

|description|

This is a simple template and example R script with docopt style options to run from the command line.
The R example dataset "mtcars" is used.


Usage and options
=================

These are based on docopt_ for R:

https://github.com/docopt/docopt.R
https://cran.r-project.org/web/packages/docopt/index.html

To run, type:
    Rscript plot_template.R -I <INPUT_FILE> [options]

Usage: plot_template.R [-I <INPUT_FILE>] [--session=<R_SESSION_NAME>]
                       [--vars=<var1_name> <var2_name>]
       plot_template.R [-h | --help]

Options:
  -I <INPUT_FILE>                 Input file name
  --session=<R_SESSION_NAME>      R session name if to be saved
  --vars=<var1_and_var2_names>    Variables to plot from input file
  -h --help                       Show this screen

Input:

    A tab separated file with headers. This is read with data.table and stringsAsFactors = FALSE

Output:

    A histogram, boxplot and scatterplot from the R dataset mtcars as three svg files.

Requirements:

    library(docopt)
    library(ggplot2)
    library(data.table)

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
# Within the script specify options as e.g.:
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
library(ggplot2)
# library(ggthemes)
library(data.table)
######################


######################
# Read files:
if (is.null(args[['-I']]) == FALSE) {
  input_name <- as.character(args[['-I']])#(args $ `-I`)
  input_data <- fread(input_name, sep = '\t', header = TRUE, stringsAsFactors = FALSE)
} else {
  # Warn or stop if arguments not given:
  warning('You need to provide an input file. This has to be tab separated with headers.',
          'Continuing with a preloaded dataset as example data.')
  #stopifnot(!is.null(args[['-I']]) == TRUE)
  # Load the example data:
  input_name <- "mtcars"
  data("mtcars")
  input_data <- data.frame(mtcars)
}
input_name

# Explore data:
class(input_data)
dim(input_data)
head(input_data)
tail(input_data)
str(input_data)
colnames(input_data)
rownames(input_data)
summary(input_data)
######################

######################
# Function to check if arguments for plotting variables were given:
# Get the named variable from the command line arguments:
cond_1 <- is.null(args[['-I']]) == FALSE
cond_2 <- is.null(args[['--vars']]) == FALSE
cond_1
cond_2

# args[['--vars']] <- "wt qsec"
get_vars(variable_name) {
  if (cond_1 == FALSE & cond_2 == FALSE) {
    vars <- strsplit(args[['--vars']], split = ' ')[[1]]
    var_1 <- vars[1]
    var_2 <- vars[2]
    print(c(vars, class(vars), var_1, var_2))
    } else {
      warning("Variable names not given, using a preloaded dataset instead")
      # Load vars from the mtcars example data:
      var_1 <- 'wt'
      var_2 <- 
    }
  }

######################

######################
####
# Histogram overlaid with kernel density curve
# http://www.cookbook-r.com/Graphs/Plotting_distributions_(ggplot2)/

# Setup:
# var1 <- 'wt'
var1
var1_label <- 'Car weight'
var1_label
plot_name <- sprintf('%s_%s_histogram', input_name, var1)
plot_name
# Plot:
ggplot(input_data, aes(x = var1)) +
       geom_histogram(aes( y = ..density..), # Histogram with density instead of count on y-axis
                 binwidth = 0.5,
                 colour = "black", fill = "white") +
       geom_density(alpha = 0.2, fill = "#FF6666") + # Overlay with transparent density plot
       ylab('density') +
       xlab(var1_label)
# Save to file:
ggsave(sprintf('%s.svg', plot_name))
# Prevent Rplots.pdf from being generated. ggsave() without weight/height opens a device.
# Rscript also saves Rplots.pdf by default, these are deleted at the end of this script.
dev.off()
####

####
# A boxplot
# Setup:
var1 <- 'cyl'
var1
var1_label <- 'Number of cylinders'
var1_label
var1_factor <- factor(input_data$var1)
var1_factor
var2 <- 'wt'
var2
var2_label <- 'Car weight'
var2_label
plot_name <- sprintf('%s_%s_%s_boxplot_2', input_name, var1, var2)
plot_name
# Plot:
ggplot(input_data, aes(x = var1_factor, y = var2, fill = var1_factor)) +
       geom_boxplot() +
       ylab(var2_label) +
       xlab(var1_label) +
       theme_classic()
# Save to file:
ggsave(sprintf('%s.svg', plot_name))
# Prevent Rplots.pdf from being generated. ggsave() without weight/height opens a device.
# Rscript also saves Rplots.pdf by default, these are deleted at the end of this script.
dev.off()
####

####
# Scatterplot and legend:
# http://www.cookbook-r.com/Graphs/Legends_(ggplot2)/
# Setup:
var1 <- 'wt'
var1
var1_label <- 'Car weight'
var1_label
var1_factor <- factor(mtcars$cyl)
var1_factor
var2 <- 'wt'
var2
var2_label <- 'Car weight'
var2_label
plot_name <- sprintf('%s_car_qsec_hp_scatterplot', input_name)
plot_name
# Plot:
ggplot(input_data, aes(x = hp, y = qsec, colour = cyl_factor)) +
       geom_point() +
       geom_smooth(method = lm) +
       ylab('1/4 mile time') +
       xlab('gross horse power') +
       labs(colour = 'number of cylinders') +
       theme_classic()
# Save:
ggsave(sprintf('%s.svg', plot_name))
# Prevent Rplots.pdf from being generated. ggsave() without weight/height opens a device.
# Rscript also saves Rplots.pdf by default, these are deleted at the end of this script.
dev.off()
####
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
