# Not optimized -exceeding time limit
def acmTeam(topic):
    # Write your code here
    max_sub = 0
    dic = {}
    m = len(topic[0])
    n = len(topic)
    for i in range(n):
        for j in range(i+1,n):
            # temp = ""
            sub_known = 0
            for k in range(m):
                if (int(topic[i][k]) or int(topic[j][k])):
                    # temp = temp+str(1)
                    sub_known += 1
                # else:
                    # temp = temp+str(0)
            dic[str(i)+','+str(j)] = sub_known
            if sub_known > max_sub:
                max_sub = sub_known
    
    team = 0
    for i in dic.keys():
        if dic[i] == max_sub:
            team += 1

    return (max_sub, team)

# still not optimized
def acmTeam2(topic):
    # Write your code here
    max_sub = 0
    team = 0
    m = len(topic[0])
    n = len(topic)
    for i in range(n-1):
        for j in range(i+1,n):
            sub_known = 0
            for k in range(m):
                if (int(topic[i][k]) or int(topic[j][k])):
                    sub_known += 1
            if sub_known > max_sub:
                max_sub = sub_known
                team = 1
            elif sub_known == max_sub:
                team +=1

    return (max_sub, team)

# working solution
def acmTeam3(topic):
    # Write your code here
    max_sub = 0
    team = 0
    m = len(topic[0])  # length of subject string
    n = len(topic)      # number os subjects
    for i in range(n-1):
        for j in range(i+1,n):
            sub_known = 0
            temp = str(int(topic[i])+int(topic[j]))
            for c in temp:
                if c!='0':
                    sub_known += 1
            if sub_known > max_sub:
                max_sub = sub_known
                team = 1
            elif sub_known == max_sub:
                team +=1

    return (max_sub, team)

print(acmTeam3(['10101','11110','00010']))

