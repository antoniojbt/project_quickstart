######################
# R script to run with docopt for command line options:
'
script_name
===========

Author: |author_names| 
Release: |version|
Date: |today|


Purpose
=======

|description|


Usage and options
=================

These are based on docopt_ for R:

https://github.com/docopt/docopt.R
https://cran.r-project.org/web/packages/docopt/index.html

To run, type:
    Rscript script_name -I <input_file>

Usage: script_name (-I <INPUT_FILE>)
       script_name [--session <R_SESSION_NAME>]
       script_name [-h | --help]
       script_name [-v | --version]

Options:
  -I             Input file name [default: this_is_a_test].
  --session      R session name if to be saved [default: FALSE].
  -h --help      Show this screen.
  -v --version   Show version [default: NA].

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

# Print docopt options and messages:
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

# Filename to save current R session, data and objects at the end:
if (args $ `--session` == TRUE) {
  save_session <- as.character(args $ `--session`)
  R_session_saved_image <- sprintf('R_session_saved_image_%s.RData', save_session)
  print(sprintf('Saving the R session as: %s', R_session_saved_image))
} else {
  print('Not saving an R session, this is the default. Specify the --session option otherwise')
}
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
if (args $ `-I` == TRUE) {
  input_name <- as.character(args $ `-I`)
  #input_data <- fread(input_name, sep = '\t', header = TRUE, stringsAsFactors = FALSE)
} else {
  # Stop if arguments not given:
  stopifnot(args $ `-I` == TRUE)
}

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
summary(input_data)
###################### 


######################
# Histogram overlaid with kernel density curve
# http://www.cookbook-r.com/Graphs/Plotting_distributions_(ggplot2)/
plot_name <- sprintf('%s_car_weight_histogram', input_name)
ggplot(input_data, aes(x = wt)) +
       geom_histogram(aes( y = ..density..), # Histogram with density instead of count on y-axis
                 binwidth = 0.5,
                 colour = "black", fill = "white") +
       geom_density(alpha = 0.2, fill = "#FF6666") + # Overlay with transparent density plot
       ylab('density') +
       xlab('weight')
ggsave(sprintf('%s.svg', plot_name))

# A boxplot:
plot_name <- sprintf('%s_car_cyl_mpg_boxplot_2', input_name)
cyl_factor <- factor(input_data$cyl)
cyl_factor
ggplot(input_data, aes(x = cyl_factor, y = wt, fill = cyl_factor)) +
       geom_boxplot() +
       ylab('weight') +
       xlab('number of cylinders') +
       theme_classic()
ggsave(sprintf('%s.svg', plot_name))

# Scatterplot and legend:
# http://www.cookbook-r.com/Graphs/Legends_(ggplot2)/
plot_name <- sprintf('%s_car_qsec_hp_scatterplot', input_name)
cyl_factor <- factor(mtcars$cyl)
cyl_factor
ggplot(input_data, aes(x = hp, y = qsec, colour = cyl_factor)) +
       geom_point() +
       geom_smooth(method = lm) +
       ylab('1/4 mile time') +
       xlab('gross horse power') +
       labs(colour = 'number of cylinders') +
       theme_classic()
ggsave(sprintf('%s.svg', plot_name))
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

# To save R workspace with all objects to use at a later time:
if (args $ `--session` == TRUE){
  print(sprintf('Saving the R session as: %s', R_session_saved_image))
  save.image(file=R_session_saved_image, compress='gzip')
} else{
  print('Did not save the R session, this is the default')
}

sessionInfo()
q()

# Next: run the script for xxx
######################
