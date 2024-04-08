n = int(input())
nums = list(map(int, input().split()))

sorted(nums)
min_diff = nums[n-1] - nums[0]
for i in range(1, len(nums)):
    if nums[i] - nums[i-1] < min_diff:
        min_diff = nums[i] - nums[i-1]
print(min_diff)