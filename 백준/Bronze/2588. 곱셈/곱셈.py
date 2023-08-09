n=int(input())
m=input()
ml=[]
ms=[]
for i in range(len(m)):ml.append(m[i])

for i in range(1,4):
    s=0
    s=n*(int(ml[3-i]))
    ms.append(s)
    print(s)
print(ms[0]+(ms[1]*10)+(ms[2]*100))