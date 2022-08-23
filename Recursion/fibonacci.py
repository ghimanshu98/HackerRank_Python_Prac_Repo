def rec_fibonacci(n, counter=0 ,f=0, l=1):
    if counter==0:
        print('{}, {}, '.format(f,l), end ='')
        rec_fibonacci(n, counter+1)
    elif counter > 0 and counter < n:
        t = f+l
        f = l
        l = t
        print('{}, '.format(t), end='')
        rec_fibonacci(n, counter+1, f, l)

def fibonacci(n):
    f = 0
    l = 1
    print('{}, {}, '.format(f,l), end='')
    for i in range(n-1):
        t = f+l
        print('{}, '.format(t), end='')
        f = l
        l = t

fibonacci(5)
print()
rec_fibonacci(5)    

