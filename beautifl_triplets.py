# not optimized
def beautifulTriplets(d, a):
    # Write your code here
    # lst = []
    count = 0
    for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                # ji = a[j]-a[i]
                # ki = a[k]-a[j]
                if a[j] - a[i] == a[k]-a[j] == d:
                    count += 1
                    # lst.append([i,j,k])

    # return len(lst)
    return count
                
def beautifulTriplets2(d,a):
    count = 0
    for i in range(len(a)-2):
        if a[i]+d in a:
            if a[i]+(2*d) in a:
                count+=1
    return count

def beautifulTriplets3(d,a):
    count = 0
    for i in range(len(a)-2):
        j = a[i]+d  # j-i = d, => j = i+d
        if j in a:
            k = d + j # k-j = d, => k = d+j, => k = d + (i+d) 
            if k in a:
                count+=1
    return count

print(beautifulTriplets3(3, [1,2,4,5,7,8,10]))