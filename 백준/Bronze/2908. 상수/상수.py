a, b=map(int, input().split())
a_list=[]
b_list=[]
for i in range(3):
    a_list.append(a%10)
    b_list.append(b%10)
    a, b = a//10, b//10
a, b = a_list[0]*100+a_list[1]*10+a_list[2]*1, b_list[0]*100+b_list[1]*10+b_list[2]*1
print(max(a,b))