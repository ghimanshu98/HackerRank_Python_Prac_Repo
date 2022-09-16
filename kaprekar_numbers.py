def iskaprakar(p):
    sq = str(p**2)
    length = len(sq)
    if len(sq)>1:
        i=0
        lim = int(length/2)
        start = ""
        while(i!=lim):
            start = start+sq[i]
            i+=1
        end = ""
        while(i!=length):
            end = end + sq[i]
            i+=1

        if int(start)+int(end) == p:
            return True
        else:
            return False
    else:
        if sq == str(p):
            return True
        else:
            return False
            
def kaprekarNumbers(p, q):
    # Write your code here
    lst = []
    for i in range(p,q+1):
        if iskaprakar(i):
            lst.append(i)
    if len(lst) >0:
        print(str(lst).replace(',', '').replace('[','').replace(']',''))
    else:
        print('INVALID RANGE')
    


# print(iskaprakar(5))
# print(iskaprakar(99))
kaprekarNumbers(1,100)