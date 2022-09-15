def rec_sum(n):
    # head recursion
    if n>0:
        return rec_sum(n-1)+n
    else:
        return 0

print(rec_sum(5))