# def stones(n,a,b):
#     # n = int(n/2)
#     tmp = []
#     t = a
#     # a+a
#     for i in range(n):
#         t = t+a
#     tmp.append(t)

#     # a+b
#     x = a
#     for i in range(n):
#         t = x+b
#         x = t
#     tmp.append(t)
               
#     # b+a
#     y = b
#     for i in range(n):
#         t = y+a
#         y = t
#     tmp.append(t)

#     # b+b
#     t = b
#     for i in range(n):
#         t = t+b
#     tmp.append(t)
#     # return sorted(set(tmp))

def stones(n,a,b):
    step = 0

    t = [0,0,0]
    for i in range(len(t)-1):
        step = t[i] + a
        t[i+1]=step
        u = [0,0,0]
        for j in range(len(u)-1):
            step2 = u[j] + b
            u[j+1] = step2



    print(t)


# print(stones(2,3,4))
stones(3,1,2)
# print(stones(4,10,100))
# print(stones(7,9,11))
