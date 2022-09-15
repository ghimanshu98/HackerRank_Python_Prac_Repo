def rec_fact(n):
    if n>0:
        return rec_fact(n-1)*n
    else:
        return 1

print(rec_fact(5))