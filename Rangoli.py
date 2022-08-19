def print_rangoli(letter):
    # your code goes here

    size = letter+letter-1

    alpha = list("abcdefghijklmnopqrstuvwxyz")

    for i in range(size):
        if(i%2==0):
            counter = letter-1
            for j in range(i, size-1):
                print('-', end=' ')
            for k in range(i+1):
                if(k%2==0):
                    print(alpha[counter], end=' ')
                    counter = counter -1
                else:
                    print('-', end=' ')

            counter=counter+2
            for l in range(i):
                if (l%2==0):
                    print('-', end=' ')
                else:
                    print(alpha[counter], end=' ')
                    counter = counter+1
            for m in range(i, size-1):
                print('-', end=' ')
            print()

    for i in range(size):
        if(i%2!=0):
            counter = letter-1
            for j in range(i+1):
                print('-', end=' ')
            for k in range(i,size-1):
                if (k%2!=0):
                    print(alpha[counter], end=' ')
                    counter = counter - 1
                else:
                    print('-', end=' ')

            counter = counter + 2 
            for l in range(i, size-2):
                if(l%2==0):
                    print(alpha[counter], end=' ')
                    counter = counter+1
                else:
                    print('-', end=' ')
            for m in range(i+1):
                print('-', end=' ')
            print()
        
    

if __name__ == '__main__':
    n = int(input("Enter Size : "))
    print_rangoli(n)