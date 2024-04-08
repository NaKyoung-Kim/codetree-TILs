a, b = map(int, input().split())

rest_cnt = [0]*b
while a > 1:
    rest = a%b
    rest_cnt[rest] += 1
    a //= b

total = 0
for rest in rest_cnt:
    total += rest ** 2
print(total)