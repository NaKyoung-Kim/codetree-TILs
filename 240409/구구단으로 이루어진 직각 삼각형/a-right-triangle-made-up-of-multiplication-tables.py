n = int(input())

for i in range(1, 6):
    for j in range(1, n+2-i):
        print("{} * {} = {}".format(i, j, i*j), end="")
        if j == n+1-i:
            print()
        else:
            print(" / ", end="")