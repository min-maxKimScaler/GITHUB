n,x=map(int, input().split())
nums=list(map(int, input().split()))
min_nums=[]

for i in range(n):
    if nums[i] < x:
        a = nums[i]
        min_nums.append(a)
    else:
        continue
for i in min_nums:
  print(i, end=" ")