import sys

n = int(sys.stdin.readline())

def process(a, b):
    total = 0
    for num in range(a, b+1):
        if num % 2 == 0:
            total+=num
    return total

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(process(a, b))