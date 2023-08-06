import math
n=int(input())
n_list=list(map(int,input().split()))

prime_num = 0
for num in n_list:
    is_prime = 0
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:is_prime += 1
        if is_prime == 0:prime_num += 1
print(prime_num)