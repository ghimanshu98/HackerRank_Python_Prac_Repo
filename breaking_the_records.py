def breakingRecords(scores):
    # Write your code here
    low, high, mini, maxi = 0, 0, scores[0], scores[0]
    for i in scores:
        if i < mini:
            # low record breaked
            mini = i
            low += 1
        elif i > maxi:
            # high record breaked
            maxi = i
            high += 1
        elif (i >mini and i<maxi) :
            # no record breaked
            pass
    return [high, low]

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)