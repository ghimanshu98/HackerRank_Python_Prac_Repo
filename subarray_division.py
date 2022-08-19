def birthday(n,lst, date, month):
    # Write your code here
    count = 0
    i = 0
    while(i<=n-month):
        # select elements equal to month
        temp = 0
        for j in range(i,i+month):
            temp = temp+lst[j]
        if temp == date:
            count = count+1
        i=i+1
    return count

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(n,s, d, m)

    print(str(result))