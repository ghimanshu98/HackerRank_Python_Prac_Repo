def split_digits(n):
    dig_lst = []
    # rev = 0
    while(n>0):
        dig = n%10
        dig_lst.append(dig)
        # rev = rev*10 + dig
        n = int(n/10)
    return dig_lst

def findDigits(n):
    # Write your code here
    count = 0
    for i in split_digits(n):
        if i!=0 and n%i==0:
            count += 1
    return count

print(findDigits(124))