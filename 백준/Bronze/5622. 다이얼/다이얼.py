s = list(input())

alpha_dict={
    ('A', 'B', 'C') : 3, ('D', 'E', 'F') : 4, ('G', 'H', 'I') : 5,
     ('J', 'K', 'L') : 6, ('M', 'N', 'O') : 7, ('P', 'Q', 'R', 'S') : 8,
      ('T', 'U', 'V') : 9, ('W', 'X', 'Y', 'Z') : 10}
time=[]
for i in s:
    for key, value in alpha_dict.items():
        if i in key:time.append(value)
print(sum(time))