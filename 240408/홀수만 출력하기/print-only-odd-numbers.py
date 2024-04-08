import sys

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num % 2 == 1 and num % 3 == 0:
        print(num)