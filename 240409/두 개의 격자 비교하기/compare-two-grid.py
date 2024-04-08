n, m = map(int, input().split())

first_list = []
second_list = []

def set_list(n, result_list):
    for _ in range(n):
        result_list.append(list(map(int, input().split())))
    return result_list

first_list = set_list(n, first_list)
second_list = set_list(n, second_list)

for i in range(n):
    for j in range(m):
        if first_list[i][j] == second_list[i][j]:
            print("0",end=" ")
        else:
            print("1", end=" ")
    print()