#!/bin/python3

import math
from operator import invert
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n,arr):
    x=arr[-1]
    y=n-2
    while(x<arr[y]) and (y>=0):
        arr[y+1]=arr[y]
        print(*arr)
        y-=1
    arr[y+1]=x
    print(*arr)
   
        # Write your code here
n=int(input("Enter the index of the array: "))
arr=[2,4,6,8,3]
(insertionSort1(n,arr))
