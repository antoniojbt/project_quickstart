#!/usr/bin/env Rscript

######################
# R script to run with docopt for command line options:
'
pq_example.R
============

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
    Rscript pq_example.R -I <INPUT_FILE> [options]

Usage: pq_example.R (-I <INPUT_FILE>) [--session=<R_SESSION_NAME>] [-O <OUTPUT_FILE>]
       pq_example.R [-h | --help]

Options:
  -I <INPUT_FILE>                 Input file name
  -O <OUTPUT_FILE>                Output file name
  --session=<R_SESSION_NAME>      R session name if to be saved
  -h --help                       Show this screen

Input:

    A tab separated file with headers. This is read with data.table
    and stringsAsFactors = FALSE
    The script is designed to take in the output of the script pq_example.py

Output:

    A tsv table with some descriptive statistics, a boxplot and a summary 
    table from a linear regression output using the R package stargazer.

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
suppressMessages(library(stargazer, quietly = TRUE)) # tables for linear regressions
######################


######################
# Read files:
if (is.null(args[['-I']]) == FALSE) {
  # args[['-I']] <- as.character('pandas_DF.tsv') # For testing
  input_name <- as.character(args[['-I']])#(args $ `-I`)
  input_data <- fread(input_name, sep = '\t', header = TRUE, stringsAsFactors = FALSE)
} else {
  # Stop if arguments not given:
  print('You need to provide an input file. This has to be tab separated with headers.')
  stopifnot(!is.null(args[['-I']]) == TRUE)
}

print('File being used: ')
print(input_name)
# Split at the last '.':
input_name <- strsplit(input_name, "[.]\\s*(?=[^.]+$)", perl = TRUE)[[1]][1]
print('Name being used to save output files: ')
print(input_name)

# Explore data, this is using data.table syntax:
# https://github.com/Rdatatable/data.table/wiki/Getting-started
# http://www.listendata.com/2016/10/r-data-table.html
class(input_data)
dim(input_data) # nrow(), ncol()
str(input_data)
input_data # equivalent to head() and tail()
setkey(input_data) # memory efficient and fast
key(input_data)
tables()
colnames(input_data)
input_data[, 2, with = FALSE] # by column position, preferable by column name to avoid silent bugs
###################### 


######################
# Process variables
str(input_data)
# The following is much simpler with a dataframe instead of a data.table though
# What you use depends on memory, preference, etc.
# To convert a data.table to a data.frame:
# setDF(input_data) # changes by reference
input_data_df <- as.data.frame(input_data) # create a new object
class(input_data_df)
class(input_data)
# Pass variables as parameters for data.table
# If re-using, automating, etc. you might want to do this, 
# so you can then specify variables fom the command line.
# Generally it's just easier (and safer and more readable) to name variables explicitely
# for project specific analysis.
# https://stackoverflow.com/questions/10675182/in-r-data-table-how-do-i-pass-variable-parameters-to-an-expression?rq=1
# Create a function:
pass_var_dt <- function(var_name) {
  a_var <- as.character(var_name)
  a_var_p <- parse(text = a_var)
}
x_var_name <- 'gender' # still needed
x_var <- pass_var_dt('gender')
head(input_data[, eval(x_var)])
# Convert variables in data.table
# https://stackoverflow.com/questions/7813578/convert-column-classes-in-data-table
x_var_factor <- as.factor(input_data[, eval(x_var)])
input_data[, c(x_var_name):= x_var_factor, with = F]
str(input_data)
str(input_data_df)

# Setup more variables:
y_var_name <- 'glucose'
y_var <- pass_var_dt('glucose')
head(input_data[, eval(y_var)])
var3_name <- 'age'
var3 <- pass_var_dt('age')
head(input_data[, eval(var3)])
######################


###################### 
# Do some stats, simple examples here:
# What's the question? What's the hypothesis?
# Descriptive:
nrow(input_data)
length(which(complete.cases(input_data) == TRUE))
summary(input_data)
summary(input_data[, c(2:3)])

# Get the mean for one var specified above:
input_data[, .(mean = mean(eval(var3), na.rm = TRUE))] # drop with and put column name, usually better practice
# Get the mean for all columns except the first one in data.table:
input_data[, lapply(.SD, mean), .SDcols = c(2:ncol(input_data))]
# Specify columns to get some summary stats (numeric variables):
colnames(input_data)
cols_summary <- c(3, 5, 6)
# Control precision for printing, can be nightmarish. Here enforce printing e.g. 0.00
# See:
# https://stackoverflow.com/questions/3443687/formatting-decimal-places-in-r
# Modified here so that FUN is function to run, x the number to format 
# and k the number of decimals to show.
# This function could/should be moved to a separate script and sourced here.
specify_decimal <- function(FUN, x, k) trimws(format(round(FUN(x, na.rm = TRUE), k), nsmall = k))

# data.table with summary stats:
desc_stats <- input_data[, sapply(.SD, function(x) c(mean = specify_decimal(mean, x, 2),
                                                     median = specify_decimal(median, x, 2),
                                                     SD = specify_decimal(sd, x, 2),
                                                     min = specify_decimal(min, x, 2),
                                                     max = specify_decimal(max, x, 2)
                                                     # quantile_25 = quantile(x, 0.25, na.rm = TRUE), # will error for non-numeric
                                                     # quantile_75 = quantile(x, 0.75, na.rm = TRUE) # will error for non-numeric
                                                     )),
                         .SDcols = cols_summary]
desc_stats

# Make a table from this:
desc_stats <- as.data.frame(desc_stats)
class(desc_stats)
# Add rownames as column with label:
desc_stats$statistics <- rownames(desc_stats)
# Re-order columns:
colnames(desc_stats)
desc_stats <- desc_stats[, c("statistics", "age", "glucose", "BMI")]
desc_stats
# Save as a file, give a name if -O option not provided:
if (is.null(args[['-O']]) == FALSE) {
  outfile <- as.character(args[['-O']])
  outfile <- sprintf('desc_stats_%s.tsv', outfile)  
} else {
  # Warn if arguments not given:
  outfile <- sprintf('desc_stats_%s.tsv', input_name)
  warning(sprintf('Outfile name not given, using a default: %s', outfile))
}
outfile
# Save file:
fwrite(desc_stats, outfile, 
            sep = '\t', na = 'NA',
            col.names = TRUE, row.names = FALSE,
            quote = FALSE)
######################


######################
# Some basic exploratory plots, no aesthetics
# Plot here or use a separate plot_template.R script (preferable if processing
# large datasets, process first, save, plot separately):
plot_name <- svg(sprintf('%s_%s_%s.svg', input_name, x_var_name, y_var_name))
par(mfrow = c(1, 3)) # rows, cols
# data.frame:
boxplot(input_data_df[,  y_var_name] ~ input_data_df[,  x_var_name])
# data.table:
boxplot(input_data[,  eval(y_var)] ~ input_data[,  eval(x_var)])
# data.frame scatterplot:
plot(input_data_df[, y_var_name] ~ input_data_df[, var3_name])
dev.off()
######################

######################
# Some inferential stats:
colnames(input_data_df)
pass_formula <- sprintf('%s ~ %s + %s', y_var_name, x_var_name, var3_name)
pass_formula
lm_input_data <- lm(formula = pass_formula, data = input_data_df)
summary(lm_input_data)

# Make a table from the output of the linear regression:
title <- as.character("Some random analysis that doesn't make sense")
stargazer(out = sprintf('%s_lm_table.html', input_name), 
          style = 'all',
          lm_input_data,
          summary = TRUE,
          title = title)

stargazer(out = sprintf('%s_lm_table.tex', input_name),
          style = 'all',
          lm_input_data,
          summary = TRUE,
          title = title)
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
print('Finished successfully.')
q()

# Next: run the script for xxx
######################
