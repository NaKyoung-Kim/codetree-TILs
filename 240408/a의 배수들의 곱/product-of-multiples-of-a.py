a, b = map(int, input().split())
c = b//a
result = 1
for i in range(1, c+1):
    result *= a*i

print(result)