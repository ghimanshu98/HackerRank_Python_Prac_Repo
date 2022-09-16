def equalizeArray(arr):
    # Write your code here
    dic = {}
    
    for i in arr:
        if dic.get(str(i)) == None:
            dic[(str(i))] = 1
        else:
            dic[str(i)] = dic.get(str(i)) + 1
    # print(dic)
    maxi = 0
    for i in dic.keys():
        print(dic[i])
        if dic[i] > maxi:
            maxi = dic[i]
    
    return len(arr) - maxi

equalizeArray([1,2,2,3])