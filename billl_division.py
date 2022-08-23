def bonAppetit(bill, k, b):
    # Write your code here
    actual = 0
    for i in range(len((bill))):
        if i != k:
            actual = actual + bill[i]
        
    actual = actual / 2
    if actual == b:
        print('Bon Appetit')
    else:
        print(b-actual)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)