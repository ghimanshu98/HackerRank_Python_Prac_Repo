#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def helper(i, j, width):
    min = width[i]
    for i in range(i+1, j+1):
        if width[i]<min:
            min = width[i]
    return min

def serviceLane(n, width, cases):
    # Write your code here
    # print(n)
    # print(width)
    # print(cases)
    temp = []
    for i in cases:
        temp.append(helper(i[0],i[1],width))        
    return temp

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    serviceLane(n, width, cases)

    # print('\n'.join(map(str, result)))
    print("")

"""
8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7

"""