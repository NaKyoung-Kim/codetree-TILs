n = int(input())

def process(n):
    if n % 2 == 0:
        return n*3 + 1
    else:
        return n*2 + 2

cnt = 0
while n < 1000:
    n = process(n)
    cnt += 1

print(cnt)