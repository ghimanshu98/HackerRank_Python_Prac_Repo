def dynamicArray(n, queries):
    # Write your code here
    two_d_arr = []
    for i in range(n):
        two_d_arr.append(list())

    last_answer = 0
    result = []
    for query in queries:
        if query[0] == 1:
            idx = ((int(query[1])^last_answer)%n)
            two_d_arr[idx].append(int(query[2]))
        elif query[0] == 2:
            idx = ((int(query[1])^last_answer)%n)
            last_answer = two_d_arr[idx][int(query[2]%len(two_d_arr[idx]))]
            result.append(last_answer)

    return result    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()