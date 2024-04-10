import sys

read = sys.stdin.readline

n = int(read())
total = 0
for i in range(n):
    total += int(read())

final = str(total)
print(final[1:]+final[0])