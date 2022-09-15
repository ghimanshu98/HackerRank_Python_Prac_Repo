from turtle import left


def appendAndDelete(s, t, k):
    # Write your code here
    t_len = len(t)
    s_len = len(s)
    if s_len == t_len:
        if k>=2*s_len:
            return "Yes"
        elif k<s_len:
            if k%2==0:
                return "Yes"
            else:
                return "No"
    elif s_len > t_len:
        i=0
        while(i<t_len):
            if s[i]==t[i]:
                i+=1
            else:    
                break
        i = i-1
        left_s_letter = s_len - i -1
        if left_s_letter > k:
            return "No"
        elif left_s_letter == k and k==t_len:  #shady
            return "Yes"
        else: # left_s_letter < k
            left_t_letter = t_len -i -1
            if left_s_letter > left_t_letter:
                if k>=2*left_t_letter+left_s_letter-left_t_letter:
                    return "Yes"
                else:
                    return "No"
    elif s_len < t_len:
        i = 0
        while(i<s_len):
            if s[i]==t[i]:
                i+=1
            else:
                break
        i = i-1
        left_t_letter = t_len -i -1
        if left_t_letter>k:
            return "No"
        elif left_t_letter == k:
            return "Yes"
        elif left_t_letter < k:
            return "Yes"


# print(appendAndDelete('hackerhappy', 'hackerrank', 9))
print(appendAndDelete('zzzzz','zzzzzzz',4))