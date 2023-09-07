for i in range(int(input())):
    sum_cnt = 0
    cnt = 1
    for k in input():
        if k == "O":
            sum_cnt += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum_cnt)