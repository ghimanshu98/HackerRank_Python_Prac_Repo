#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    height = 1
    if n%2==0: # even cycles
        for i in range(int(n/2)):
            height = 2*height+1
    else:
        for i in range(int(n/2)):
            height = 2*height+1
        height = 2*height+1 # for last odd cycle
    return height

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(str(result) + '\n')

    # fptr.close()
