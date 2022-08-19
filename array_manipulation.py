def arrayManipulation(n, queries):
    # Write your code here - this logic works but time consuming
    lst = [0]*n
    max = None
    # for i in range(n):
    #     lst.append(0)

    for query in queries:
        for i in range(query[0]-1, query[1]):
            lst[i] = lst[i] + query[2]
            if max == None:
                max = lst[i]
            elif lst[i]>max:
                max = lst[i]

    return (lst,max)

def arrayManipulation2(n, queries):
    # Write your code here - this logic works but time consuming
    lst = [None]*n
    max = None
    # for i in range(n):
    #     lst.append(0)
    for query in queries:
        for i in range(query[0]-1, query[1]):
            if lst[i] != None:
                lst[i] = lst[i] + query[2]
                if max == None:
                    max = lst[i]
                elif lst[i]>max:
                    max = lst[i]
            else:
                lst[i] = query[2]
                if max == None:
                    max = lst[i]
                elif lst[i]>max:
                    max = lst[i]
    return (lst,max)

from operator import add

def arrayManipulation3(n, queries):
    # Write your code here - this logic works but time consuming
    lst = [0]*n
    max = None

    for query in queries:
        low = query[0]-1
        upp = query[1]
        lst[low:upp] = list(map(add, lst[low: upp], [query[2]]*(upp-low+1)))
    
    return lst

def arrayManipulation3(n, queries):
    # Write your code here - this logic works but time consuming
    lst = [0]*n
    max = None

    for query in queries:
        low = query[0]-1
        upp = query[1]
        lst[low:upp] = list(map(add, lst[low: upp], [query[2]]*(upp-low+1)))
        
    
    return lst    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation3(n, queries)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
