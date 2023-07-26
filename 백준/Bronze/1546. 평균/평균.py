import sys
n=int(input())
score=list(map(int, sys.stdin.readline().split()))
ns=[]
m=max(score)
for i in score:
    i = i/m*100
    ns.append(i)
print(sum(ns)/n)