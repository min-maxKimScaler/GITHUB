scoreList=[list(map(int, input().split())) for i in range(5)]
max_score=0
index=0

for i in range(len(scoreList)):
    tmp=0
    tmp=sum(scoreList[i])
    if tmp > max_score:max_score=tmp;index=i+1
print(f'{index} {max_score}')