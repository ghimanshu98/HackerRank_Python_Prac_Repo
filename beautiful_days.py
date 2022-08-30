def reverse(num):
    rev = 0
    while(num>0):
        rev = rev*10 + (num%10)
        num = int(num/10)
    return rev

def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j+1):
        if (x-reverse(x))%k == 0:
            count += 1
    return count


beautifulDays(20,23,6)