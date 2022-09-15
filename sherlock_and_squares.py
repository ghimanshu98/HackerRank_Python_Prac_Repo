from math import sqrt


import math

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

print(squares(11,724))
    