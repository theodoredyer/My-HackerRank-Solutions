#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    tally = 101*[0]
    for i in range(0, n):
        tally[ar[i]] += 1
    #print(tally)
    
    for j in range(0, 101):
        while(tally[j] >= 2):
            tally[j] -= 2
            pairs += 1
            
    return pairs

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 5, 7, 7, 9, 10, 11]))
