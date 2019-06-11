##################################################
# Dockerfile for project_quickstart 
# https://github.com/AntonioJBT/project_quickstart
##################################################


############
# Base image
############

# FROM python:3-onbuild 
# FROM ubuntu:17.04

FROM jfloff/alpine-python
# https://github.com/jfloff/alpine-python
# This is a minimal Python 3 image that can start from python or bash

# Or simply run:
# docker run --rm -ti jfloff/alpine-python bash
# docker run --rm -ti jfloff/alpine-python python hello.py

# An interactive shell based on Debian with miniconda3 is:
# docker pull continuumio/miniconda3
# docker run -i -t continuumio/miniconda3 /bin/bash

#########
# Contact
#########
MAINTAINER Antonio Berlanga-Taylor <a.berlanga@imperial.ac.uk>


#########################
# Update/install packages
#########################

# Install system dependencies
# For Alpine see:
# https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management
RUN apk update && apk upgrade \
    && apk add \
    tree \
    sudo \
    vim \
    vimdiff

#    wget \
#    bzip2 \
#    unzip \
#    git \ # Already in Alpine Python

#####
# If running the example pipelines:
# Cairo graphics libraries are needed for svg plots.
# On Debian images run eg:
#apt-get update
#apt-get upgrade
#apt-get install
#apt-get clean

# Then install packages to allow apt to use a repository over HTTPS:
#apt-get install \
#    apt-transport-https \
#    ca-certificates \
#    curl \
#    gnupg2 \
#    software-properties-common \
#    sudo

# For cairo libraries run:
#sudo apt-get install libcairo2-dev

# Install inkscape:
#sudo apt install inkscape

#####

#########################
# Install Python packages
#########################

RUN pip install --upgrade pip setuptools \
    && pip install flake8 pytest \
    && pip list

#########################
# Install package to test 
#########################

RUN cd /home \
    && git clone https://github.com/AntonioJBT/project_quickstart.git \
    && cd project_quickstart \
    && python setup.py install \
    && cd ..


###############################
# Install external dependencies
###############################


############################
# Default action to start in
############################
# Only one CMD is read (if several only the last one is executed)
#ENTRYPOINT ['/xxx']
#CMD echo "Hello world"
#CMD project_quickstart.py
CMD ["/bin/sh"]

# Create a shared folder between docker container and host
#VOLUME ["/shared/data"]
