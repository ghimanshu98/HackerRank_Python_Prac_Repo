def score(word, lst):
    score = 0
    for s in lst:
        temp = word
        count, index = 0, 0
        while(index <= len(word)):
            temp = temp[index:]
            index=temp.find(s)
            # index = index + 
            if index > -1:
                count = count +1
                index = index + 1
            else:
                break
        score =score + count
    return score

def minion_game(word):
    # your code goes here
    # word = "BANANA"
    vowels = list("AEIOU")
    sub_list = []
    stu_lst, kev_lst = [], []

    # creating substrings
    i=0
    while(i<len(word)):
        j=i
        while(j<len(word)):
            temp = word[i:j+1]
            if temp not in sub_list:
                sub_list.append(temp)
            j = j+1
        i=i+1

    # filtering substrings
    for s in sub_list:
        if s[0] in vowels:
            kev_lst.append(s)
        else:
            stu_lst.append(s)

    # scoring
    kev_sc, stu_sc = score(word, kev_lst), score(word, stu_lst)
    if stu_sc > kev_sc:
        print('Stuart '+str(stu_sc))
    elif stu_sc < kev_sc:
        print('Kevin '+str(kev_sc))
    else:
        print('DRAW')
    
    print('Stuart '+str(stu_sc))
    print('Kevin '+str(kev_sc))

if __name__ == '__main__':
    s = input()
    minion_game(s.upper())


    # The code works but not optimzed.