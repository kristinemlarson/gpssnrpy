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

* RINEX v 2.11 observation filename

* RINEX v 2.11 navigation filename

* output filename

* SNR choice (99, 66, 88, 50) as defined at the gnssrefl website

and then:

* transRinex rinexname navname output 99

I have provided two smallish files you can use to test the code:

* transRinex p1011500.20o auto1500.20n p1011500.snr 99



I am still working on this documentation

Kristine M. Larson
