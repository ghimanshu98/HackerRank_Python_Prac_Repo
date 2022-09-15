#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxi = None
    for i in range(0,len(arr)-2):  # for sliding window row wise
        for j in range(0,len(arr)-2):  # for sliding window column wise
            sum = 0
            flag = False
            for k in range(i, i+3):
                # flag = False
                for l in range(j, j+3):
                    if flag==False:
                        sum = sum + arr[k][l]
                        # print(arr[k][l], end=' ')
                        if l == j+2:
                            flag = True
                            continue
                    if flag ==True:
                        # if l == l+1
                        # print(' ', end=' ')
                        sum = sum + arr[k][l+1]
                        # print(arr[k][l+1], end=' ')
                        flag = False
                        # print()
                        break
                    # flag = True
                # print()
            # print(sum)
            if maxi == None:
                maxi = sum
            elif sum>maxi:
                maxi = sum

    return maxi
    

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(str(result))
