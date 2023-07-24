# 영수증에 적힌 총 금액 X 입력받음
X = int(input())

# 영수증에 적히 구매한 물건의 종류의 수 N 입력받음
N = int(input())

# 더한 금액을 저장할 sum 초기화
sum = 0

# 구매한 물건의 종류의 수 N만큼 순회
for i in range(N):
    # a,b 값을 받아옴
    a,b = map(int, input().split())
    # 금액 * 갯수 = sum에 저장하면서 지속적으로 더함
    sum += a*b

if X == sum:
  print("Yes")
else:
  print("No")