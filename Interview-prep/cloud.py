#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    curpos = 0
    jumps = 0

    while(curpos < len(c)):
        if(curpos + 3 >= len(c)):
            jumps += 1
            curpos += 2
            break
        elif(c[curpos + 2] == 0):
            jumps += 1
            curpos += 2
        else:
            jumps += 1
            curpos += 1

    return jumps
# End jumpingOnClouds

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))