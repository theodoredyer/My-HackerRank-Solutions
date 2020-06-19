#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    occurances = 0
    perstring = 0
    perlen = len(s)

    if(n < perlen):
        for i in range(0, n):
            if(s[i:i+1] == 'a'):
                occurances += 1
        return occurances

    for i in range (0, len(s)):
        if(s[i:i+1] == 'a'):
            perstring += 1
    occurances = (perstring * ((int) (n / perlen)))
    #print(occurances)
    
    if(n % perlen != 0 and n > perlen):
        #print('not even')
        left = n % perlen
        #print(left)
        for i in range(0, left):
            if(s[i:i+1] == 'a'):
                occurances += 1

    return occurances
# End repeatedString
    

print(repeatedString('aaaa', 3))

