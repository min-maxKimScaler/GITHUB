alphaL=[input() for _ in range(5)]

for j in range(15):
    for i in range(len(alphaL)):
        if j < len(alphaL[i]):
            print(alphaL[i][j],end='')