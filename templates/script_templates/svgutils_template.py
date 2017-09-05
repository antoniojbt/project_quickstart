##############
# Examples from svgutils
# https://neuroscience.telenczuk.pl/?p=331
# http://svgutils.readthedocs.io/en/latest/tutorials/composing_multipanel_figures.html
# http://cairosvg.org/
# Use inkscape instead of cairo?
##############


##############
#####
import svgutils as su # compose, transform, templates
import cairosvg
import sys
import os
#####

#####
#create new SVG figure:
fig = su.transform.SVGFigure("16cm", "6.5cm")

# load svg figures (preferably matpotlib-generated):
fig1 = su.transform.fromfile('sigmoid_fit.svg')
fig2 = su.transform.fromfile('anscombe.svg')
# Test also simply:
#imported_svg1 = '/path_to/XXXX.svg'
#imported_svg2 = '/path_to/XXXX.svg'


# get the plot objects:
plot1 = fig1.getroot()
plot2 = fig2.getroot()
plot2.moveto(280, 0, scale=0.5)

# add text labels:
txt1 = su.transform.TextElement(25,20, "A", size=12, weight="bold")
txt2 = su.transform.TextElement(305,20, "B", size=12, weight="bold")

# append plots and labels to figure
fig.append([plot1, plot2])
fig.append([txt1, txt2])

# save generated SVG files
fig.save("fig_final.svg")

# Convert SVG file to PDF:
cairosvg.svg2pdf(url='fig_final_compose.svg', write_to='fig_final_compose.pdf')
#inkscape --export-pdf=fig_final.pdf fig_final.svg
#####

#####
#CONFIG['figure.save_path'] = 'composing_multipanel_figures'

Figure("16cm", "6.5cm",
       Panel(
             Text("A", 25, 20, size=12, weight='bold'),
             SVG("sigmoid_fit.svg")
            ),
       Panel(
             Text("B", 25, 20).move(280, 0),
             SVG("anscombe.svg").scale(0.5)
             ).move(280, 0),
#             Grid(20, 20)
       ).tile(2, 1)
        .save("F{}_{}.svg".format(figure_number, figure_legend))
# Convert SVG file to PDF:
cairosvg.svg2pdf(url='fig_final_compose.svg', write_to='fig_final_compose.pdf')
#inkscape --export-pdf=fig_final.pdf fig_final.svg
#####
##############

##############
quit()
##############