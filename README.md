### gpssnrpy

-[Installation](#installation)
-[Usage](#usage)
-[RINEX downloader](#download RINEX files)
-[ORBIT downloader](#download ORBIT files)
-[Future work and acknowledgements](#future work)

This library will allow python users easy access to RINEX translators 
currently only provided in Fortran (gpsSNR.f and gnssSNR.f).  This 
first version is a port of gpsSNR.f.  I have also included some utilities
that I originally packaged with [gnssrefl](https://github.com/kristinemlarson/gnssrefl).  

## Installation

* git clone https://github.com/kristinemlarson/gpssnrpy

* cd into gpssnrpy, set up a virtual environment and activate it.

* pip install .


## Usage

Inputs:

* RINEX v2.11 observation filename
* output filename
* RINEX v2.11 navigation filename
* SNR choice (99, 66, 88, 50) as defined at the gnssrefl website

Optional
* -dec decimation (seconds)

Sample usage: 

*gpssnr rinexname outputname navname 99*

*gpssnr rinexname outputname navname 99 -dec 30*


I have provided a small obs file (and nav file) you can use to test the code:

* gpssnr p1011500.20o p1011500.snr auto1500.20n  99 


## download RINEX files

*download_rinex station year month day* 

code can also be called as *download_rinex station year doy 0*

station must be four character, lower case, and the default is RINEX version 2.11 and low-rate files.
Please use -h to find out how to download high rate or version 3.

Optional:

* archive  

These are currently supported archives: sopac, unavco, sonel, cddis, nz, ga, bkg, ngs, nrcan 

**You need to install CRX2RNX for true access to these RINEX files.  It should be stored in a 
folder with the environment variable EXE**


## download orbit files

*download_orbits src year month day*

Sample usage: 

*download_orbits nav 2020 150 0*  is nav file for year 2020 and day of year 150

*download_orbits nav 2020 12 31*  is nav file for December 31 in the year 2020 

orbit sources (src) currently allowed (lowercase):

* nav : GPS broadcast, perfectly adequate for reflectometry.
* igs : IGS precise, GPS only
* igr : IGS rapid, GPS only
* jax : JAXA, GPS + Glonass, within a few days, very reliable
* gbm : GFZ Potsdam, multi-GNSS, not rapid
* grg: French group, GPS, Galileo and Glonass, not rapid
* wum : Wuhan, multi-GNSS, not rapid


## work to do

I am still working on this documentation. I will be adding instructions 
on how to use these as libraries.

Kristine M. Larson
https://kristinelarson.net

Thank you to the developers of numpy for providing excellent documentation for f2py 
and [raxod502](https://github.com/raxod502) for his package management help!

