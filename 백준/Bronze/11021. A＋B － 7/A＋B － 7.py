T = int(input())
sum_T = 0

for i in range(T):
    A,B = map(int, input().split())
    sum_T = A+B
    print(f"Case #{i+1}: {sum_T}")