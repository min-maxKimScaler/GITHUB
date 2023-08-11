n,m=map(int, input().split())
al=[]
bl=[]

for i in range(n):
    i=list(map(int,input().split()))
    al.append(i)

for i in range(n):
    i=list(map(int,input().split()))
    bl.append(i)

for i in range(n):
    for j in range(m):print(al[i][j] + bl[i][j], end=' ')
    print()