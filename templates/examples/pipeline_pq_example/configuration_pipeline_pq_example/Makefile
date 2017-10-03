########
# Minimal makefile for Sphinx documentation
# Modified for project_quickstart templates
########


########
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = pq_example 
SOURCEDIR     = .
BUILDDIR      = _build
########


########
# TO DO:
# Download, convert SVG images for PDF outputs

# Variables for image building and linking
# See example:
# https://sites.google.com/site/nickfolse/home/sphinx-latexpdf-output-with-svg-images
IMAGEDIR      = _images ../
# SVG to PDF conversion:
SVG2PDF       = inkscape
SVG2PDF_FLAGS = --without-gui --export-area-drawing --file=$< --export-pdf=$@
########


########
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean 
########


########
# Pattern rule for converting SVG to PDF:
%.pdf: %.svg
	$(SVG2PDF) $(SVG2PDF_FLAGS)
#	$(SVG2PDF) -f $< -A $@

# Build a list of SVG files to convert to PDFs:
PDFs := $(foreach dir, $(IMAGEDIRS), $(patsubst %.svg,%.pdf,$(wildcard $(SOURCEDIR)/$(dir)/*.svg)))

# Make a rule to build the PDFs:
images: $(PDFs)
#@echo 'Converting SVGs to PDFs'
########


########
# Create a clean target to delete old builds and images:
# PDFs not built from the source SVG files will not be deleted.
clean:
	-rm -rf $(BUILDDIR)/*
	-rm -f $(PDFs)
########


########
# Add dependencies to these targets:
latex: $(PDFs)

latexpdf: $(PDFs)
# Use my_image.* (instead of my_image.svg) in your .rst source files to make Sphinx automagically
# choose the appropriate image format for the target build.
########


########
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
########
