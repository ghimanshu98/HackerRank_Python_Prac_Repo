# Optimized 
def circularArrayRotation2(arr, rotation, queries= None):
    # Write your code here
    arr_length= len(arr)
    if rotation < arr_length:
        temp_holder = []
        
        for i in range(arr_length- rotation, arr_length):
            temp_holder.append(arr[i])
        print(temp_holder)

        for i in range(arr_length-rotation, 0, -1):
            arr[i+rotation-1] = arr[i-1]

        # adding last values to the array
        for i in range(len(temp_holder)):
            arr[i] = temp_holder[i]

    elif rotation > arr_length:
        round = int(rotation/arr_length)
        rotation = rotation - round*arr_length
        return circularArrayRotation2(arr, rotation, queries)

    res = []
    for i in queries:
        res.append(arr[i])

    return res


# Un Optimized - taking O(n^2) time
def circularArrayRotation(arr, rotation, queries= None):
    for i in range(rotation):
        last = arr[len(arr)-1]
        for j in range(len(arr)-1, 0,-1):
            arr[j] = arr[j-1]
        arr[0] = last
        print('{} rotation : {}'.format(i,arr))

    res = []
    for q in queries:
        res.append(arr[q])
    return res

# for i in range(1,6):
#     circularArrayRotation2([1,2,3,4,5], i)

arr = []
print(circularArrayRotation2([1,2,3,4,5],2,[1]))
print(circularArrayRotation2([1,2,3,4,5],7,[1]))