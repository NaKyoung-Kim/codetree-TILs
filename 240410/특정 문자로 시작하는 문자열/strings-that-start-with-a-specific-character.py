import sys

read = sys.stdin.readline
strs = []
n = int(read())

for i in range(n):
    strs.append(read().strip())

lower = read()
cnt = 0
length = 0

for i in range(0, n):
    if strs[i].startswith(lower):
        cnt += 1
        length += len(strs[i])
print('{} {:.2f}'.format(cnt, length/cnt))