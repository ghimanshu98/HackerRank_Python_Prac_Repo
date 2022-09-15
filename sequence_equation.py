def return_index(p, i):
    for x in range(len(p)):
        if p[x]==i:
            return x+1

def permutationEquation(p):
    # Write your code here
    n = 0
    for i in p:
        if i>n:
            n = i

    res = []
    for i in range(1,n+1):
        res.append(return_index(p,return_index(p, i)))

    return res


print(permutationEquation([2,3,1]))