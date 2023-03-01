
# Third-party libraries
import re
import math as m
import numpy as np

# local libraries
import datahandle
import constants as c
def calc_JD(dateTime):

    # DD:MM:YYYY:HH:MM:SS~
    dateDict = datahandle.string_to_dict(
        dateTime, 
        ['D', 'M', 'Y', 'h', 'm', 's']
        )
    
    J0 = 367 * dateDict['Y'] - m.floor((7 * (dateDict['Y'] + m.floor((dateDict['M'] + 9) / 12))) / 4) + \
        m.floor((275 * dateDict['M'])/9) + dateDict['D'] + 1721013.5

    UT = (dateDict['h'] + dateDict['m'] / 60 + dateDict['s'] / 3600) / 24
    JD = J0 + UT
    return JD

def kepler_E(e, M):
    # This function uses Newton’s method to solve Kepler’s
    # equation E - e*sin(E) = M for the eccentric anomaly,
    # given the eccentricity and the mean anomaly.

    # E - eccentric anomaly (radians)
    # e - eccentricity, passed from the calling program
    # M - mean anomaly (radians), passed from the calling program
    # pi - 3.1415926...

    # tolerance
    error = 1*10**-8

    # starting value for E:
    if M < m.pi:
        E = M + e/2
    else:
        E = M - e/2
    
    # iterate until E is determined within error tolerance 
    ratio = 1
    while abs(ratio) > error:
        ratio = (E - e*m.sin(E) - M) / (1 - e*m.cos(E))
        E = E - ratio

    return E