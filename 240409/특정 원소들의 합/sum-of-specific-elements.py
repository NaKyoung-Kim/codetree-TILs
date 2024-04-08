num_list = []
for _ in range(4):
    nums = list(map(int, input().split()))
    num_list.append(nums)

total=0
for i in range(4):
    for j in range(i+1):
        total += num_list[i][j]
print(total)