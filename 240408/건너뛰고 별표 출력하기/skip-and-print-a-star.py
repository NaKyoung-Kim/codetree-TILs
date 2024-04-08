n = int(input())
flag=0
cnt = 1

for i in range(4*n-3):
    if i % 2 != 0:
        print()
        continue
    if flag == 0:
        print("*"*cnt)
        if i == 8:
            flag = 1
            cnt -= 1
        else:
            cnt += 1
    else:
        print("*"*cnt)
        cnt -= 1