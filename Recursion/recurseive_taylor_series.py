def rec_fact(n):
    if n==0:
        return 1
    else:
        return rec_fact(n-1)*n

def rec_power(m,n):
    if n==0:
        return 1
    elif n%2==0: # if n is even
        return rec_power(m*m, n/2)
    elif n%2!=0: # if n is odd
        return rec_power(m*m, int(n-1)/2) * m

def rec_taylor(x, n):
    if n==0:
        return 1
    else:
        return rec_taylor(x, n-1) + rec_power(x, n)/rec_fact(n)       

print(rec_taylor(2,4))
