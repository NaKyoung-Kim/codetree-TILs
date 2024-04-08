n = int(input())

for j in range(n, 0, -1):
    for i in range(j, n+1):
        print(i, end=" ")
    print()