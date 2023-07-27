chess=list(map(int, input().split()))
empty=[]
for i in chess[0:2]:
  if i==1:empty.append(1-i)
  else:empty.append(1-i)
for i in chess[2:5]:
  if i==2:empty.append(2-i)
  else:empty.append(2-i)
for i in chess[5:6]:
  if i==8:empty.append(8-i)
  else:empty.append(8-i)
for i in empty:print(i,end=' ')