from functools import reduce

lst = [2,3,5,1,7,5,9,10,20]

# filter function
evens = list(filter((lambda x: x%2==0), lst))

print("Evens : ", evens)

# map function
doubles = list(map(lambda x: x*2, evens))

print("Doubles of evens : ", doubles)

# reduce function
sum = reduce((lambda x,y: x+y), doubles)

print("Sum of doubles : ", sum)