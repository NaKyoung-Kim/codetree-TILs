import sys

flag = 1
for i in range(5):
    n = int(sys.stdin.readline())
    if n % 3 != 0:
        flag=0

print(flag)