.. include:: report_substitution_vars.rst

##############
|project_name|
##############


Authored by:

|all_author_names|

Date: |date|

Keywords: |keywords|

version = |version|

Licensed as |license|

Check the project at:

|project_url|

Correspondence to: |author_email|


See rst-basics_ for webpages and tutorials.

.. _rst-basics: https://github.com/EpiCompBio/welcome/blob/master/rst_basics.rst


Introduction
############

|short_description|


You can include other rst files. See the toctree_ directive:

.. _toctree: http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#include-other-rst-files-with-the-toctree-directive


Results
#######

Result 1


Include a figure, e.g.:

.. figure:: ../F1_mtcars.*

    This is from "../F1_mtcars.*"


Or:

.. figure:: ../F1_mtcars.*
   :height: 100
   :width: 200
   :scale: 50
   :alt: A multi-panel plot from the R dataset mtcars


See image_ directive full markup.

.. _image: http://docutils.sourceforge.net/docs/ref/rst/directives.html#images


Or import a figure which can have a caption and whatever else you add:


.. figure:: ../F2_mtcars.*
   :align: center

   This is a multi-panel plot from the file F2_mtcars.*


PDF files can be included as a clickable download e.g. :download:`F1_mtcars.pdf file <../F1_mtcars.pdf>`


Include a table as a file here:


Don't abuse the raw directive. Embedding html for an html output works, but not
for a pdf output. The files "../my_dataframe_lm_table.html" won't appear
in a pdf for instance.

Preferable to output tables as csv or tsv and use::

   .. csv-table::
   :file: ../desc_stats_my_dataframe.tsv
   :delim: tab


to embed results in either html or pdf output.


.. raw:: html
   :file: ../my_dataframe_lm_table.html


.. raw:: html
   :file: ../mtcars_lm_table.html


.. csv-table::
   :file: ../desc_stats_my_dataframe.tsv
   :delim: tab

References
##########

Code used is available at |project_url|

References, e.g. [CIT2002]_ are defined at the bottom of the page as::

  .. [CIT2002] A citation

and called with::

  [CIT2002]_
