'''
script_name
===========

:Author: |author_name|
:Release: |version|
:Date: |today|


Purpose
=======

|description|

Make a figure layout using svgutils

Usage and options
=================

These are based on docopt_, see examples_.

.. _docopt: https://github.com/docopt/docopt

.. _examples: https://github.com/docopt/docopt/blob/master/examples/options_example.py


Usage:
       script_name [--plot1]
       script_name [--plot1]
       script_name [-O FILE]
       script_name [-h | --help]
       script_name [-V | --version]
       script_name [-f --force]
       script_name [-L | --log]

Options:
    --plot1        
    -O             Output file name.
    -h --help      Show this screen
    -V --version   Show version
    -f --force     Force overwrite
    -L --log       Log file name.

Documentation
=============

    For more information see:

        |url|

    Also see examples and information from svgutils:

    - https://neuroscience.telenczuk.pl/?p=331
    - http://svgutils.readthedocs.io/en/latest/tutorials/composing_multipanel_figures.html
    - https://svgutils.readthedocs.io/en/latest/compose.html
    - http://cairosvg.org/
    - https://inkscape.org/en/

'''
############
import sys
import os
import docopt

from svgutils.compose import *
import cairosvg
import os
############

############
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
# Finish and exit with docopt arguments:
if __name__ == '__main__':
    arguments = docopt(__doc__, version='xxx 0.1')
    print(arguments)
    sys.exit(main())
############
