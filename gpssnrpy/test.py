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
    newfangled way to send character arrays to fortran using f2py
    yippeee
    input is a string - output is bytes?
    """
    j=bytes(string,'ascii') + b'\0\0'

    return array(j)




def main():
    """
    command line interface for download_rinex
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("rinex", help="rinexname", type=str)
    parser.add_argument("nav", help="navfile", type=str)
    parser.add_argument("output", help="outputfile", type=str)
    parser.add_argument("filetype",   help="e.g. 66, 99", type=str)

    args = parser.parse_args()


#   assign to normal variables
    rinexfile = args.rinex 
    snrname = args.output
    orbit = args.nav 
    snrtype = args.filetype

    if snrtype not in ['99', '66','50','88','77']:
        print('Illegal snrtype choice',  snrtype)
        sys.exit()

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
