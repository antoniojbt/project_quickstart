See rst-basics_ for webpages and tutorials.

.. _rst-basics: https://github.com/EpiCompBio/welcome/blob/master/rst_basics.rst


#############
pq_example
#############

-----

author1, author2, author3 …

affiliation1, affiliation2, affiliation3 …

Correspondence should be addressed to:

Keywords:

Running title:


Introduction
############

Include other rst files::

  .. toctree::
      :maxdepth: 2
      :numbered:
      :titlesonly:
      :glob:
      :hidden:

      report_pipeline_pq_example.rst

See the toctree_ directive for full info.

.. _toctree: http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#include-other-rst-files-with-the-toctree-directive


Results
#######

Result 1

.. Glob all legends*.rst files:

.. toctree::
    :glob:
    
     F*.svg


Include an image::

  .. image:: images/ball1.gif
  
Or::

  .. image:: images/xxx.png
    :height: 100
    :width: 200
    :scale: 50
    :alt: alternate text

See image_ directive full markup.

.. _image: http://docutils.sourceforge.net/docs/ref/rst/directives.html#images

Or import a figure which can have a caption and whatever else you add::

  .. figure:: mtcars_scatterplot_lm.svg
      :width: 200px
      :align: center
      :height: 100px
      :alt: alternate text
      :figclass: align-center
      
      a caption would be written here as plain text. You can add more with eg::
  
    .. code-block:: python

        import image

Include a simple csv table::

  .. csv-table:: a title
     :header: "name", "firstname", "age"
     :widths: 20, 20, 10
     
     "Smith", "John", 40
     "Smith", "John, Junior", 20

See csv-table_ directive for example.

.. _csv-table: http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#the-csv-table-directive


Code used is available at |project_url|

References
##########

References, e.g. [CIT2002]_ are defined at the bottom of the page as::

  .. [CIT2002] A citation

and called with::

  [CIT2002]_


