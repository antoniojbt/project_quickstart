October 11, 2017

Dockerfiles currently don't work because of a mix of installation issues:

- In both, installing svglite is problematic. See error log below.
- In Debian continuum "conda install icu" gives version 54 but 58 is needed.
conda-forge channel has the correct version but various installs and commands
with conda seem to fail.
- "pip install cgat" in Debian continuum also fails. I haven't left an error log
for this.

I will try again at some point.



svglite error:
##############
root@57539c9365c8:/home/pq_example/results# R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("svglite", repos = "http://cran.us.r-project.org") ; library("svglite")' 

R version 3.3.2 (2016-10-31) -- "Sincere Pumpkin Patch"
Copyright (C) 2016 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> source("https://bioconductor.org/biocLite.R") ; install.packages("svglite", repos = "http://cran.us.r-project.org") ; library("svglite")
Bioconductor version 3.4 (BiocInstaller 1.24.0), ?biocLite for help
A new version of Bioconductor is available after installing the most recent
  version of R; see http://bioconductor.org/install
also installing the dependency ‘gdtools’

trying URL 'http://cran.us.r-project.org/src/contrib/gdtools_0.1.6.tar.gz'
Content type 'application/x-gzip' length 35263 bytes (34 KB)
==================================================
downloaded 34 KB

trying URL 'http://cran.us.r-project.org/src/contrib/svglite_1.2.1.tar.gz'
Content type 'application/x-gzip' length 41315 bytes (40 KB)
==================================================
downloaded 40 KB

* installing *source* package ‘gdtools’ ...
** package ‘gdtools’ successfully unpacked and MD5 sums checked
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
/opt/conda/lib/R/bin/config: 1: eval: make: not found
Using PKG_CFLAGS=
Using PKG_LIBS=-lcairo
------------------------- ANTICONF ERROR ---------------------------
Configuration failed because cairo was not found. Try installing:
 * deb: libcairo2-dev (Debian, Ubuntu)
 * rpm: cairo-devel (Fedora, CentOS, RHEL)
 * csw: libcairo_dev (Solaris)
 * brew: cairo (OSX)
If cairo is already installed, check that 'pkg-config' is in your
PATH and PKG_CONFIG_PATH contains a cairo.pc file. If pkg-config
is unavailable you can set INCLUDE_DIR and LIB_DIR manually via:
R CMD INSTALL --configure-vars='INCLUDE_DIR=... LIB_DIR=...'
--------------------------------------------------------------------
ERROR: configuration failed for package ‘gdtools’
* removing ‘/opt/conda/lib/R/library/gdtools’
* restoring previous ‘/opt/conda/lib/R/library/gdtools’
* installing *source* package ‘svglite’ ...
** package ‘svglite’ successfully unpacked and MD5 sums checked
** libs
sh: 1: make: not found
ERROR: compilation failed for package ‘svglite’
* removing ‘/opt/conda/lib/R/library/svglite’

The downloaded source packages are in
	‘/tmp/Rtmpslb5Vr/downloaded_packages’
Updating HTML index of packages in '.Library'
Making 'packages.html' ... done
Warning messages:
1: In install.packages("svglite", repos = "http://cran.us.r-project.org") :
  installation of package ‘gdtools’ had non-zero exit status
2: In install.packages("svglite", repos = "http://cran.us.r-project.org") :
  installation of package ‘svglite’ had non-zero exit status
Error in library("svglite") : there is no package called ‘svglite’
Execution halted
##############
