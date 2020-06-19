#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    trackpos = 0
    valleys = 0
    for i in range(0, n):
        if(s[i:i+1] == 'D'):
            trackpos -= 1
            print(trackpos)
        elif(s[i:i+1] == 'U'):
            trackpos += 1
            if(trackpos == 0):
                valleys += 1
            print(trackpos)
    return valleys
# End contingValleys

print(countingValleys(8, 'UDDDUDUU'))