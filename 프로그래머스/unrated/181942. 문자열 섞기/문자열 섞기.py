def solution(str1, str2):
    tmp=[]
    for i in range(len(str1)):tmp.append(str1[i]+str2[i])
    answer=''.join(tmp)
    return answer