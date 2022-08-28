def rec_pow(m,n):
    if n>0:
        return rec_pow(m, n-1)*m
    else:
        return 1


def opt_rec_pow(m,n):
    if n==0:
        return 1
    if (n%2==0): # if even - then one multiply and power half
        return opt_rec_pow(m*m, n/2)
    else: # it is odd then 
        return opt_rec_pow(m*m, (n-1)/2) * m

print(rec_pow(2,3))
print(opt_rec_pow(2,3))