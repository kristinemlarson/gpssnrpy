### gpssnrpy

This library will allow python users easy access to RINEX translators 
currently only provided in Fortran (gpsSNR.f and gnssSNR.f).  This 
first version is a port of gpsSNR.f.  

### to install 

* git clone https://github.com/kristinemlarson/gpssnrpy

* cd into gpssnrpy, set up a virtual environment and activate it.

* pip install .


### to run from the commandline


Inputs:

* RINEX v2.11 observation filename
* output filename
* RINEX v2.11 navigation filename
* SNR choice (99, 66, 88, 50) as defined at the gnssrefl website

Optional
* -dec decimation (seconds)

Thus this translates and decimates to 30 seconds:

* gpssnr rinexname outputname navname 99 -dec 30

or translates it all:

* gpssnr rinexname outputname navname 99 

I have provided a small obs file (and nav file) you can use to test the code:

* gpssnr p1011500.20o p1011500.snr auto1500.20n  99 -dec 30



I am still working on this documentation

Kristine M. Larson

Thank you to the developers of numpy for providing excellent documentation for f2py 
and [raxod502](https://github.com/raxod502) for his package management help!

