A = input()
B = input()

n = 0
while A != B:
    n += 1
    A = A[-1]+A[:-1]
    if n >= len(A):
        n = -1
        break

print(n)