a, b = map(int, input().split())

def seq(n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return seq(n-1) + 2*(seq(n-2))

for i in range(1, 11):
    print(seq(i), end=" ")