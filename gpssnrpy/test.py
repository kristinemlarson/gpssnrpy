# -*- coding: utf-8 -*-
"""
downloads RINEX files
kristine larson
2020sep03 - modified environment variable requirement
need to make this f2py -c -m gpssnr.gpssnr gpssnrpy/gpssnr.f
"""
import argparse
import os
import sys
from numpy import array
import gpssnrpy.gpssnr as gpssnr



def binary(string):
    """
    changes python string to bytes for use in
    fortran code using f2py
    """
    j=bytes(string,'ascii') + b'\0\0'

    return array(j)




def main():
    """
    command line interface for running gpssnr from python
    inputs are the two inputs (obs and nav), output, and snr choice
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("rinex", help="rinexname", type=str)
    parser.add_argument("nav", help="navfile", type=str)
    parser.add_argument("output", help="outputfile", type=str)
    parser.add_argument("filetype",   help="e.g. 50, 66, 88, 99", type=str)

    args = parser.parse_args()


#   assign inputs to normal variable names
    rinexfile = args.rinex 
    snrname = args.output
    orbit = args.nav 
    snrtype = args.filetype

    # these are allowed choices
    if snrtype not in ['99', '66','50','88']:
        print('Illegal snrtype choice',  snrtype)
        sys.exit()

    # check that inputs exist before calling code
    if os.path.isfile(rinexfile) and os.path.isfile(orbit):
        in1 = binary(rinexfile); in2 = binary(snrname);
        in3 = binary(orbit); in4 = binary(snrtype)
        gpssnr.foo(in1,in2,in3,in4)
        if os.path.isfile(snrname):
            print('SUCCESS: SNR file created',snrname)
    else:
        if not os.path.isfile(rinexfile):
            print('RINEX file does not exist', rinexfile)
        if not os.path.isfile(orbit):
            print('Orbit file does not exist', orbit)
        sys.exit()


if __name__ == "__main__":
    main()
