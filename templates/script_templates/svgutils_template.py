##############
# Examples from svgutils
# https://neuroscience.telenczuk.pl/?p=331
# http://svgutils.readthedocs.io/en/latest/tutorials/composing_multipanel_figures.html
# https://svgutils.readthedocs.io/en/latest/compose.html
# http://cairosvg.org/
# Use inkscape instead of cairo?
##############


############
# First generate some example data to make this script runnable
# This is modified from 
# http://users.ecs.soton.ac.uk/jn2/teaching/pythonLecture.html

import matplotlib.pyplot as plt
import random

# Make a first example plot:
popSize = 100
category1 = []
category2 = []

# Start by generating scores for category 1 individuals
# Their mean score is 95
for i in range(popSize):
    category1.append(random.normalvariate(95,10))

# Now generate scores for category 2 individuals
# They have a higher mean of 105
for i in range(popSize):
    category2.append(random.normalvariate(105,10))

scores = [category1,category2]

plt.boxplot(scores)
plt.savefig('boxplots.svg')
plt.savefig('boxplots.pdf')
plt.close()

# Make a second example plot:
x = []
y = []

sampleSize = 500

for i in range(sampleSize):
    newVal = random.normalvariate(100,10)
    x.append(newVal)
    y.append(newVal / 2.0 + random.normalvariate(50,5))

plt.scatter(x,y,c="red",marker="s")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.savefig("scatter2.svg")
plt.savefig('scatter2.pdf')
plt.close()
############


############
# Make the actual panel with svgutils
from svgutils.compose import *
import cairosvg
import os

# Names of the plots to read in, these have to be svg files:
plot1 = 'boxplots.svg' # These are taken from above as example data
plot2 = 'scatter2.svg'

# Name the figure panel (which will be "F{figure_number}_{figure_name}.{format}", 
# Only svg can be output with svgutils:
figure_number = '1'
figure_name = 'test'
file_format_in = 'svg'
file_format_out = 'pdf'
layout_name_1 = str('F{}_{}.{}'.format(figure_number,
                                       figure_name,
                                       file_format_in))
layout_name_2 = str('F{}_{}.{}'.format(figure_number,
                                       figure_name,
                                       file_format_out))

my_layout = Figure("21cm", "19cm", # A4 paper is 210 mm x 197 mm
                  # Panel() groups all elements belonging to one plot/panel
                  Panel(
                      SVG(plot1).scale(0.8), # scale only the plot, not the text
                      # Place Text() after SVG(), otherwise it doesn't plot:
                      Text("A", 25, 20, size = 11, weight = 'bold'),
                      ).move(0, 10),
                  Panel(
                      SVG(plot2).scale(0.8),
                      Text("B", 25, 20, size = 11, weight = 'bold'),
                      ).move(340, 10), # placed here move() is applied to all
                                       # elements of the panel
                                       # move(280, 0) will move the figure 280
                                       # px horizontally
                  #Grid(20, 20) # Generates a grid of horizontal and vertical lines 
                               # labelled with their position in pixel units
                               # Use to test if figure is placed correctly, then
                               # comment out. Use within Figure()
                               # e.g. Figure(XXX, Grid(20, 20), Panel(XXX))
                    )
                     #.tile(2, 1) # (ncols, nrows), use before .save()
                     #.tile() errors, see:
                     #https://stackoverflow.com/questions/45850144/is-there-a-bug-in-svgutils-compose-module-regarding-the-arrangement-of-figures/45863869#45863869

# Save the Figure:
my_layout.save(layout_name_1)

# Convert SVG file to PDF with CairoSVG:
cairosvg.svg2pdf(url = layout_name_1,
                 write_to = layout_name_2
                 )

# Alternatively with inkscape:
#os.system('''inkscape --export-pdf=F{}_{}.ink.{} {}'''.format(figure_number,
#                                                              figure_name,
#                                                              file_format_out,
#                                                              layout_name_1)
#          )

# Inkscape is very power and has many more options, e.g. 
# --export-background=white --export-area-drawing
# See:
#https://inkscape.org/sk/doc/inkscape-man.html


# TO DO: How to add legends directly?
# Otherwise pull into an rst file and add there. 
############

############
quit()
##############
