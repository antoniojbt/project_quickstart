#!/usr/bin/env Rscript

######################
# R script to run with docopt for command line options:
'
plot_pq_example_mtcars.R
========================

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
    Rscript plot_pq_example_mtcars.R [--session=<R_SESSION_NAME>]

Usage: plot_pq_example_mtcars.R [--session=<R_SESSION_NAME>]
       plot_pq_example_mtcars.R [-h | --help]

Options:
  --session=<R_SESSION_NAME>      R session name if to be saved
  -h --help                       Show this screen

Input:

    None needed, the script loads the already available mtcars dataset.

Output:

    A histogram, boxplot and scatterplot as three svg files.

Requirements:

    library(docopt)
    library(ggplot2)


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
# Load a previous R session, data and objects, e.g.:
# load('R_session_saved_image_R_plotting_test.RData', verbose=T)
######################


######################
# Import libraries
 # source('http://bioconductor.org/biocLite.R')
library(ggplot2)
library(grid)
# library(ggthemes)
library(data.table)
######################


######################
# Load the example data:
input_name <- "mtcars"
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
# Create your own ggplot2 theme or see ggthemes package
# https://cran.r-project.org/web/packages/ggthemes/vignettes/ggthemes.html
# http://sape.inf.usi.ch/quick-reference/ggplot2/themes
# The following is modified from:
# https://stackoverflow.com/questions/31404433/is-there-an-elegant-way-of-having-uniform-font-size-for-the-whole-plot-in-ggplot
# If re-using functions it is much better to copy this to a new script and run here as:
# source('my_ggplot_theme.R')
theme_my <- function(base_size = 14, base_family = "Times") {
  normal_text <- element_text(size = as.numeric(base_size), colour = "black", face = "plain")
  large_text <- element_text(size = as.numeric(base_size + 1), colour = "black", face = "plain")
  bold_text <- element_text(size = as.numeric(base_size + 1), colour = "black", face = "bold")
  axis_text <- element_text(size = as.numeric(base_size - 1), colour = "black", face = "plain")
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(legend.key = element_blank(),
          strip.background = element_blank(),
          text = normal_text,
          plot.title = bold_text,
          axis.title = large_text,
          axis.text = axis_text,
          legend.title = bold_text,
          legend.text = normal_text,
          #plot.margin = grid::unit(c(1,1,1,1),"mm")
          plot.margin = grid::unit(c(1,1,1,1), "mm")
          )
  }
theme_my()
######################

######################
####
# Histogram overlaid with kernel density curve
# http://www.cookbook-r.com/Graphs/Plotting_distributions_(ggplot2)/

# Setup:
x_var <- 'wt'
x_var_label <- 'Car weight'
plot_name <- sprintf('%s_%s_histogram.svg', input_name, x_var)
plot_name
# Plot:
ggplot(input_data, aes(x = input_data[, x_var])) +
       geom_histogram(aes( y = ..density..), # Histogram with density instead of count on y-axis
                 binwidth = 0.5,
                 colour = "black", fill = "white") +
       geom_density(alpha = 0.2, fill = "#FF6666") + # Overlay with transparent density plot
       ylab('density') +
       xlab(x_var_label) +
       theme_my()
       # theme_classic() +
       # theme(text = element_text(size = 12),
       #  legend.position = 'none') # Place after theme_"style"()
# Save to file:
ggsave(plot_name)
# Prevent Rplots.pdf from being generated. ggsave() without weight/height opens a device.
# Rscript also saves Rplots.pdf by default, these are deleted at the end of this script.
dev.off()
####

####
# A boxplot
# Setup:
x_var <- 'cyl'
x_var_label <- 'Number of cylinders'
x_var_factor <- factor(input_data[, x_var])
x_var_factor
y_var <- 'wt'
y_var_label <- 'Car weight'
plot_name <- sprintf('%s_%s_%s_boxplot_2.svg', input_name, x_var, y_var)
plot_name
# Plot:
ggplot(input_data, aes(x = x_var_factor, y = input_data[, y_var], fill = x_var_factor)) +
       geom_boxplot() +
       ylab(y_var_label) +
       xlab(x_var_label) +
       theme_my() +
       theme(legend.position = 'none') # Place after theme_"style"()
             # text = element_text(size = 12) # Change text size
# Save to file:
ggsave(plot_name)
# Prevent Rplots.pdf from being generated. ggsave() without weight/height opens a device.
# Rscript also saves Rplots.pdf by default, these are deleted at the end of this script.
dev.off()
####

####
# Scatterplot and legend:
# http://www.cookbook-r.com/Graphs/Legends_(ggplot2)/
# Setup:
x_var <- 'hp'
x_var_label <- 'Gross horse power'
grouping_var <- 'cyl'
grouping_var <- factor(input_data[, grouping_var])
y_var <- 'qsec'
y_var_label <- '1/4 mile time'
legend_label <- 'Number of cylinders'
plot_name <- sprintf('%s_%s_%s_scatterplot.svg', input_name, x_var, y_var)
plot_name
# Plot:
ggplot(input_data, aes(x = input_data[, x_var], y = input_data[, y_var], colour = grouping_var)) +
       geom_point() +
       geom_smooth(method = lm) +
       ylab(y_var_label) +
       xlab(x_var_label) +
       labs(colour = legend_label) +
       theme_my()
# Save:
ggsave(plot_name)
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
print('Finished successfully')
q()

# Next: run the script for xxx
######################
