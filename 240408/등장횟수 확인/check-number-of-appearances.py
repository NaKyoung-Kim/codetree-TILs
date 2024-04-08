import sys

result = 0
for i in range(5):
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        result += 1
print(result)