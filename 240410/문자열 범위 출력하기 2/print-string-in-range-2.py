char_list = input()
n = int(input())
cnt = 0

for char in reversed(char_list):
    if cnt >= n:
        break
    print(char,end="")
    cnt += 1