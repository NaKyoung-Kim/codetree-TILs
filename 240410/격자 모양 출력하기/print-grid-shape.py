import sys

n,m = map(int, sys.stdin.readline().split())

nums = [[0]*n for _ in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    nums[i-1][j-1] = i*j

for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()