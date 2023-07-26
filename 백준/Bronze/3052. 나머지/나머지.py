num_list=[]
l = []
for i in range(10):
    nums = int(input())
    num_list.append(nums)
for i in num_list:
    a = i%42
    l.append(a)
print(len(list(set(l))))