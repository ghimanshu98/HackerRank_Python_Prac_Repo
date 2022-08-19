
def angryProfessor(k, a):
    # Write your code here
    sat = 0
    for i in a:
        if i<=0:
            sat = sat+1
    
    if sat>=k:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        number_of_students = int(first_multiple_input[0])

        threshold_student = int(first_multiple_input[1])

        arrival_time = list(map(int, input().rstrip().split()))

        result = angryProfessor(threshold_student, arrival_time)

        print(str(result) + '\n')

