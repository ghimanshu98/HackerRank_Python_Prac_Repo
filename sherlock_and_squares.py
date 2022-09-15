from math import sqrt


import math
from re import I

# not optimized
def squares2(a, b):
    # Write your code here
    count = 0
    for i in range(a,b+1):
        temp = int(math.sqrt(i))
        if(temp*temp == i):
            count+=1
    return count

# not optimized
def squares(a, b):
    count = 0
    for i in range(1,b+1):
        sq = i**2
        if sq >=a and sq <= b:
            count += 1

    return count

# Working and optimied code
def squares3(a,b):
    if a==1:
        count = 1
    else:
        count = 0
    i, j, jc = 1, 2, 2
    while(i<b):
        i = i + j + 1
        if i >=a  and i<=b:
            count += 1
        j = 2*jc
        jc += 1

    return count

print(squares3(1,10))
# print(squares3(4,4))    