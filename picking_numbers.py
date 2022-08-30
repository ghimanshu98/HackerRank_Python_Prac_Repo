#!/bin/python3

import math
from operator import mod
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# No Optimized - 3 test cases failed out of 10
length = 2
def pickingNumbers(arr, level=0):
    global length
    sub_arrays = []
    for i in range(level, len(arr)-1):
        temp = []
        if level !=0:
            temp = arr[0:level]
        for j in range(i, len(arr)):
            # print('{} - {} = {}'.format(arr[j], arr[i], arr[j]-arr[i]))
            if abs(arr[j]-arr[i])<=1:
                temp.append(arr[j])
        sub_arrays.append(temp)
    # print(sub_arrays)
    if len(sub_arrays) == 0:
        if length < len(arr):
            length = len(arr)
        return None
    level += 1
    for i in sub_arrays:
        if len(i)>=2:
            # level += 1
            pickingNumbers(i,level)

def count(arr, i):
    temp = 0
    for x in arr:
        if x==i:
            temp+=1
    return temp

# Fully working code with less complexity and easily understandable
def pickingNumbers2(arr):
    temp = []
    for i in range(len(arr)):
        neg = (count(arr, arr[i]-1))
        neu = (count(arr, arr[i]))
        pos = (count(arr, arr[i]+1))
        temp.append(neg+neu)
        temp.append(neu+pos)
    print(max(temp))

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # pickingNumbers(a)
    pickingNumbers(a)
    print(str(length) + '\n')
