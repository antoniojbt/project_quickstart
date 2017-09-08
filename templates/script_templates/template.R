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


Usage:
       script_name [--main-method]
       script_name [-I FILE]
       script_name [-O FILE]
       script_name [-h | --help]
       script_name [-V | --version]
       script_name [-f --force]
       script_name [-L | --log]

Options:
    -I             Input file name.
    -O             Output file name.
    -h --help      Show this screen
    -V --version   Show version
    -f --force     Force overwrite
    -L --log       Log file name.


Input: 


Output:


Requirements:


Documentation
=============

    For more information see:

    |url|

' -> doc

# Print docopt options and messages:
library(docopt, quietly = TRUE)
# Retrieve the command-line arguments:
opt <- docopt(doc, version = 0.1)
# See:
# https://cran.r-project.org/web/packages/docopt/docopt.pdf
# https://www.slideshare.net/EdwindeJonge1/docopt-user2014
# http://rgrannell1.github.io/blog/2014/08/04/command-line-interfaces-in-r/
# docopt(doc, args = commandArgs(TRUE), name = NULL, help = TRUE,
# version = NULL, strict = FALSE, strip_names = !strict,
# quoted_args = !strict)

# Print to screen:
str(opt)
######################


######################
# Logging
# This can be taken care of by CGAT Experiment.py if running as a pipeline.
# Otherwise there seem to be few good alternatives. A workaround is this code:
# logging.R
# In the script_templates dir of project_quickstart.
# It does not run on it own though, needs copy/pasting for now.


# Re-load a previous R session, data and objects:
#load('R_session_saved_image_order_and_match.RData', verbose=T)

# Filename to save current R session, data and objects at the end:
R_session_saved_image <- paste('R_session_saved_image_','.RData', sep='')
R_session_saved_image
######################


######################
# Import libraries:
library(data.table)
######################


######################
# TO DO: change to docopt:
#Set-up arguments:

some_var <- as.character(args[1])
another_var <- as.numeric(args[2])
######################



######################
# Read files:
input_file <- fread(input_file, sep = ' ', header = TRUE, stringsAsFactors = FALSE)
head(input_file)
tail(input_file)
dim(input_file)
str(input_file)
summary(input_file)
class(input_file)
######################


######################
# Get one of the example data sets in R:
data()

######################


######################
# Plot here or use a separate plot_template.R script (preferable if processing
# large datasets, process first, save, plot separately):
plot_name <- svg(paste(plot_name, '.svg', sep = ''))
plot(plot_name)
dev.off()
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

# To save R workspace with all objects to use at a later time:
save.image(file=R_session_saved_image, compress='gzip')

sessionInfo()
q()

# Next: run the script for xxx step
######################
