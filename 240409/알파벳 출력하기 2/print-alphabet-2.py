n = int(input())
# print(ord("A")) # 65
# print(ord("Z")) # 90

# print(chr(ord("A")))

num = 65
for i in range(n):
    for j in range(1, 2*n):
        if i*2 < j and j % 2 != 0:
            if num == 91:
                num = 65
            print(chr(num), end="")
            num += 1
        else:
            print(" ", end = "")
    print()

# i: 1~n
#     i 번째 줄에는 n-i+1개의 알파벳이 있다.
#     j: 1~2n-1
#     이 알파벳들은 j의 값이 홀수인 곳에 있고,
#     i<j 이면 안나와  


# 11 / 13
# 23

# 11/13/15
# 23/25
# 35