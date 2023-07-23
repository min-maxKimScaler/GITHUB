a,b,c = map(int, input().split())

if a==b and a==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+c*100)
else:
    # max 함수를 사용하여 최댓값을 곱해줌
    print(100* max(a,b,c))