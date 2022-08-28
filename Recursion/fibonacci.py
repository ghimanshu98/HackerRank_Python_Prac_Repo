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

# gives the nth term in fibonacci series
def rec_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return rec_fib(n-2)+ rec_fib(n-1)

fibonacci(5)
print()
rec_fibonacci(5)    
print()
print(rec_fib(5))
