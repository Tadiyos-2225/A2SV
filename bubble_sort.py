#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count=0
    for b in range(len(a)):
        for c in range(len(a) - b - 1):
            if a[c]>a[c+1]:
                a[c]=a[c+1]
                a[c+1]=a[c]
        count = count + 1
    
    print("First Element: " , a[0] )
    print("Last Element: " , a[-1])
    print("The soretd element is: ",a)
            # Write your code here
a=[2,5,6,7,8,12]
countSwaps(a)
