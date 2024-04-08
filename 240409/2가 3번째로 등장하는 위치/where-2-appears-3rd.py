n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, len(nums)+1):
    if nums[i-1] == 2:
        cnt += 1
    if cnt == 3:
        print(i)
        break