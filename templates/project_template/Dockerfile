#######################################################
# Dockerfile for pipeline 
# https://github.com/
#######################################################


####################################################
# Base image is from Ubuntu 16.04 aka 'Xenial Xerus'
# Provide Python 2.7.12
####################################################
# TO DO: update to py3.5

FROM ubuntu:16.04

##########
# Contact:
##########
MAINTAINER Antonio Berlanga-Taylor <a.berlanga@imperial.ac.uk>

#########################
# Update/install packages
#########################

RUN apt-get update && apt-get install -y \
	apt-transport-https \
	curl \
	git \
	graphviz \
 	libxml2-dev \
 	libcurl4-openssl-dev \
	python-pip \
	software-properties-common \ 
	sudo \
	unzip \
	vim \
	bzip2 \
	fixincludes \
	wget && \
  	rm -rf /var/lib/apt/lists/*


# System dependencies needed for CGAT packages/dependencies:
#    bzip2 \
#    fixincludes



############
# CGAT tools
############

# Install CGAT code
RUN wget --no-check-certificate https://raw.github.com/CGATOxford/cgat/master/install-CGAT-tools.sh && \
    mkdir /shared && \
    bash install-CGAT-tools.sh --cgat-devel --zip --location /shared

# TO DO: install CGATPipelines
# https://github.com/CGATOxford/cgat/blob/master/Dockerfile
# https://github.com/CGATOxford/CGATPipelines/blob/master/INSTALL


#########################
# Install Python packages
#########################

# install RUFFUS:
# TO DO: Not needed as should be in requirements for cgat tools and CGATPipelines
# Leaving for now though

RUN pip install --upgrade pip
RUN pip install ruffus --upgrade


###############################
# Install external dependencies
###############################

# install PLINK:

#ENV PLINK_VERSION       1.9
#ENV PLINK_NO		  plink170113
#ENV PLINK_HOME          /usr/local/plink

#RUN wget https://www.cog-genomics.org/static/bin/$PLINK_NO/plink_linux_x86_64.zip && \
#    unzip plink_linux_x86_64.zip -d /usr/local/ && \
#    rm plink_linux_x86_64.zip && \
#    cd /usr/local/bin && \
#    ln -s $PLINK_HOME plink

#############################
# Install R (currently 3.3.2)
#############################

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
RUN apt-get update && apt-get install -y r-base r-cran-littler 

# Create install script for packages that uses biocLite:

RUN 	echo '#!/usr/bin/env r' > /usr/local/bin/install.r && \
	echo 'library(utils)' >> /usr/local/bin/install.r && \	
  	echo 'source("https://bioconductor.org/biocLite.R")' >> /usr/local/bin/install.r && \
	echo 'lib.loc <- "/usr/local/lib/R/site-library"' >> /usr/local/bin/install.r && \ 
	echo 'biocLite(commandArgs(TRUE), lib.loc)' >> /usr/local/bin/install.r && \
	chmod 755 /usr/local/bin/install.r

# install required R packages:

RUN Rscript /usr/local/bin/install.r \
	ggplot2 \
	data.table

###############
# Housekeeping:
###############

# This from David M.'s ITMAT Dockerfile example:
#ENV USER datasci
#ENV HOME /home/$USER

#RUN useradd -ms /bin/bash $USER && \
#	echo "$USER:DaTaSc1" | chpasswd && \
#	adduser $USER sudo

########################
# Set the default action
########################

# Examples:
# Set environment variables (this is from cgat tools):
# ENV PATH=/shared/conda-install/envs/cgat-devel/bin:$PATH

# Set up entrypoint:
#ENTRYPOINT ["plink"]
#CMD ["--help"]

# Add an entry point to the cgat command:
# ENTRYPOINT ["/shared/conda-install/envs/cgat-devel/bin/cgat"]

# Create a shared folder between docker container and host
#VOLUME ["/shared/data"]




