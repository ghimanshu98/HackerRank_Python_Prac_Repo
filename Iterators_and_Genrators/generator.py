# get an iterator for top ten perfect squares

def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

sq_it = topten() # will return a generator obj

for i in sq_it:
    print(i)