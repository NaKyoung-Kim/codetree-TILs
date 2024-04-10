n = int(input())

nums = list(map(int, input().split()))

def bubble(nums):
    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
    return nums

for i in range(0, n-1):
    for num in bubble(nums):
        print(num, end=" ")
    print()