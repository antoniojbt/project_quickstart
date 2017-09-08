'''
script_name
===========

:Author: |author_name|
:Release: |version|
:Date: |today|


Purpose
=======

|description|


Usage and options
=================

These are based on docopt_, see examples_.

.. _docopt: https://github.com/docopt/docopt

.. _examples: https://github.com/docopt/docopt/blob/master/examples/options_example.py


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

Documentation
=============

    For more information see:

        |url|

'''
############
import sys
import os
import docopt

import matplotlib.pyplot as plt
import random
############

############
# Generate some example data to make this script runnable
# This is modified from 
# http://users.ecs.soton.ac.uk/jn2/teaching/pythonLecture.html

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
############

############
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
# Finish and exit with docopt arguments:
if __name__ == '__main__':
    arguments = docopt(__doc__, version='xxx 0.1')
    print(arguments)
    sys.exit(main())
############
