def getFactor(brr):
    set_fact = None
    for i in brr:
        set_temp = set()
        for j in range(1, int((i/2)+1)):
            if i%j==0:
                set_temp.add(j)
        set_temp.add(i)
        if set_fact == None:
            set_fact = set_temp
        else:
            set_fact = set_fact.intersection(set_temp)
    return set_fact

def check_fact(arr_a, considerd_int):
    temp = []
    for i in arr_a:
        print(temp)
        for j in considerd_int:
            if j%i==0:
                if j not in temp:
                    temp.append(j)
            else:
                if j in temp:
                    temp.remove(j)
        considerd_int = temp.copy()
    return temp



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    considered_int = getFactor(brr)

    count = len(check_fact(arr, considered_int))

    print(str(count) + '\n')

