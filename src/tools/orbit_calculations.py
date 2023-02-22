import re
import math as m
import numpy as np

# local libraries
import datahandle

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
