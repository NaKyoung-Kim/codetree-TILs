n = int(input())

num_list = list(map(int, input().split()))
num_list.reverse()

for num in num_list:
    if num % 2 == 0:
        print(num, end=" ")