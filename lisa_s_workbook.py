def workbook(n, k, arr):
    page = 1
    sp = 0
    for i in arr:
        ch_qu = i
        tq = 0
        q = 1
        if ch_qu <=k:
            while(tq < k and q<=ch_qu):
                if q == page:
                    sp += 1
                q +=1
                tq += 1
            page += 1
            tq = 0
        else: # if ch_qu > k
            while(q<=ch_qu):
                tq = 0
                while(tq < k and q<=ch_qu):
                    if q == page:
                        sp += 1
                    q += 1
                    tq += 1
                page += 1
    return sp



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(str(result) + '\n')


"""
5 3
4 2 6 1 10
"""