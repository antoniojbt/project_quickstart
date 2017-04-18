##################################################
# Dockerfile for project_quickstart 
# https://github.com/AntonioJBT/project_quickstart
##################################################


############
# Base image
############

# FROM python:3-onbuild 
# FROM ubuntu:17.04
# 
FROM jfloff/alpine-python
# https://github.com/jfloff/alpine-python
# This is a minimal Python 3 image that can start from python or bash

# Or simply run:
# docker run --rm -ti jfloff/alpine-python bash
# docker run --rm -ti jfloff/alpine-python python hello.py

#########
# Contact
#########
MAINTAINER Antonio Berlanga-Taylor <a.berlanga@imperial.ac.uk>


#########################
# Update/install packages
#########################

# Install system dependencies
#RUN apt-get update && apt-get install -y \
#    wget \
#    bzip2 \
#    fixincludes \
#    unzip \
#    git \
#    vim \
#    wget

#	apt-transport-https \
#	curl \
#	graphviz \
# 	libxml2-dev \
# 	libcurl4-openssl-dev \
#	python-pip \
#	software-properties-common \ 
#	sudo \


#########################
# Install package to test 
#########################

RUN cd home \
    && git clone https://github.com/AntonioJBT/project_quickstart.git \
    && cd project_quickstart \
    && python setup.py install \
    && cd ..


#########################
# Install Python packages
#########################

#RUN pip install --upgrade pip

###############################
# Install external dependencies
###############################


############################
# Default action to start in
############################

#ENTRYPOINT ['/project_quickstart']
#CMD echo "Hello world"
CMD ["/bin/sh"]

# Create a shared folder between docker container and host
#VOLUME ["/shared/data"]
