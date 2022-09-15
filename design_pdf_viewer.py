#!/bin/python3

import math
import os
import random
import re
from string import ascii_lowercase
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

# ascii - of a is 65
def designerPdfViewer(h, word):
    # Write your code here
    alpha = ascii_lowercase
    max_height = 0
    i = 0
    try:
        while word[i]!='':
            temp = h[alpha.find(word[i])]
            if temp >max_height:
                max_height = temp
            i += 1
    except IndexError:
        return i*max_height

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')

    # fptr.close()
