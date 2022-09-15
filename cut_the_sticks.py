def zero_remover(arr):
    new_arr = []
    for i in arr:
        if i!=0:
            new_arr.append(i)
    return new_arr

# using python functions
def cutTheSticks(arr):
    # Write your code here
    iter = []
    while(len(arr)>=1):
        iter.append(len(arr))
        mini = min(arr)
        arr = [i-mini for i in arr]
        arr = zero_remover(arr)
        # arr.remove(0)

    return iter



# cutTheSticks([1,2,3])
cutTheSticks([5,4,4,2,2,8])