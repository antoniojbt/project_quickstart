#######################################
Substitutions in restructuredText files 
#######################################

Variables are specified as "|xxxx|".

An example would be:

The main file, e.g.:

.. code-block:: rst

   .. Include templates from external file (this is a comment).
   .. include:: substitution_vars.rst

   I can include text, like |my custom text|, from other files.

   I can include such as the following: |more text| 

   And |here|.


Then specify the substitutions in a separate rst file, such as "substitution_vars.rst".

.. code-block:: rst

   .. Fill in the variables in the external rst file:

   .. |my custom text| replace:: "example text 1"

   .. |more text| replace:: several other things as well

   .. |here| replace:: bla bla bla

Because the substitution process uses the ".. include:: " directive, everything in the file will get included. Thus use hidden comments if needed.

Use rst2pdf to render, which will then substitute the variables with the appropriate changes. pandoc doesn't seem to read the include directive properly. rst2pdf runs in Python 2.7 only.

Run: 

.. code-block:: bash

   rst2pdf file_with_include.rst -o file_with_include.pdf 


See SO question_ and `technical documenation`_ for more information.   

.. _question: http://stackoverflow.com/questions/9772228/docutils-restructuredtext-template-features

.. _`technical documenation`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions
