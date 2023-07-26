n,m=map(int,input().split())
basket=[]
for i in range(n):
    a = i+1
    basket.append(a)
for row in range(m):
    i,j=map(int,input().split())
    basket[j-1], basket[i-1] = basket[i-1],basket[j-1]
for i in basket:
    print(i,end=' ')