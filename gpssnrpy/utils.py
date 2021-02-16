# some utilities - mostly GPS/GNSS related
# author: kristine larson
# date: February 14, 2021

from numpy import array

def binary(string):
    """
    changes python string to bytes for use in
    fortran code using f2py via numpy
    input is a string, output is bytes with null at the end
    """
    j=bytes(string,'ascii') + b'\0\0'

    return array(j)

