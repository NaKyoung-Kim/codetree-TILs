n = int(input())

num_list = []

for i in range(n-1, -1, -1):
    ith_list = []
    for j in range(0,n):
        ith_list.append(0)
        if j == 0:
            ith_list[j] = i+1
        elif j % 2 == 0:
            ith_list[j] = ith_list[0] + 2*(j//2)*n
        elif j == 1:
            ith_list[j] = 2*n+1-ith_list[0]
        else:
            ith_list[j] = ith_list[1] + 2*(j//2)*n
    num_list.append(ith_list)

for i in range(0,n):
    for j in range(n-1,-1,-1):
        print(num_list[i][j], end=" ")
    print()