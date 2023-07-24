import sys

T = int(input())

sum_T = 0

for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    sum_T = A+B
    print(sum_T)