import sys
numcount=int(sys.stdin.readline())
count=0

for i in range(0,numcount):
    N=sys.stdin.readline().strip()
    answer=1
    for i in range(0,len(N)):
        a=N[i]
        if i+1 <len(N):
            if N[i]==N[i+1]:pass
            else:
                for c in range(i+1,len(N)):
                    if N[c]==a:
                        answer=0
                        break
    if answer==1:count=count+1
print(count)