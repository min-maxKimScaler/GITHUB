a = int(input())
for i in range(a):
  b = a-i-1
  for j in range(a):
    j = 2*i + 1
  print(" "*(b)+"*" * j)