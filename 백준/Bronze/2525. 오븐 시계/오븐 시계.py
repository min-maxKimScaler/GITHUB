A,B = map(int, input().split())
C = int(input())

if C%60 == 0:
    # B에 영향을 미치지 않아 A만 변경하면 됨
    # A+몫 = 24를 넘고 최대 23+17=40 -> 0~16까지 출력 가능
    if A+int(C/60) >= 24:
        print(f"{A+int(C/60)-24} {B}")
    # A+몫 = 24 안넘는다면 그냥 출력하면 됨
    else:
        print(f"{A+int(C/60)} {B}")
# 나머지가 0으로 떨어지지 않는 경우 = 59 119 사례
else:
    # 위와 동일
    if A+int(C/60) >= 24:
        # 기존 B분 + C 나머지 더해서 60 넘으면 A에 +1해야 함
        if B+int(C%60) >= 60:
            print(f"{A+int(C/60)-24+1} {B+int(C%60)-60}")
        # 기존 B분 + C 나머지 더해서 60 안 넘으면 A는 그대로 임
        else:
            print(f"{A+int(C/60)-24} {B+int(C%60)}")
    # A+몫 = 24를 안 넘긴다면 그냥 출력해도 됨
    # 그러나 예외 케이스가 있음 A 12 B 50분 C 190분 3시간 10분 
    # B+C 나머지가 60 넘길 때 A에 1을 더해줘야 함
    else:
        if B+(C%60) >= 60:
            if A+int(C/60)+1 >= 24:
                print(f"{A+int(C/60)+1-24} {B+int(C%60)-60}")
            else:
                print(f"{A+int(C/60)+1} {B+int(C%60)-60}")
        else:
            print(f"{A+int(C/60)} {B+int(C%60)}")