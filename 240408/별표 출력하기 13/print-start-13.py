n = int(input())
upper = list(range(n, 0, -1))
lower = list(range(1, n+1))


for i in range(len(upper)):
    print("* "*upper[i])
    print("* "*lower[i])