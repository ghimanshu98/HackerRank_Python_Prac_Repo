def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    flag = 0
    valley = 0
    mountain = 0
    down_flag = False
    up_flag = False
    for i in path:
        if i == 'U':
            flag = flag +1
            up_flag = True
            if down_flag == True and flag== sea_level:
                valley = valley +1
                up_flag, down_flag = False, False
        elif i=='D':
            flag = flag -1
            down_flag = True
            if up_flag == True and flag == sea_level:
                mountain = mountain + 1
                up_flag, down_flag = False, False
    return valley


if __name__ == '__main__':


    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result) + '\n')