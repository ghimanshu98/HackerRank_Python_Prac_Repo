def fairRations(arr):
    # Write your code here
    count = 0
    even_flag = False
    for i in range(len(arr)-1):
        if arr[i]%2 != 0:
            arr[i] = arr[i] + 1
            arr[i+1] = arr[i+1] + 1
            count += 2
    if count>0:
        return str(count)
    else:
        return "NO"

print(fairRations([4,5,6,7]))


