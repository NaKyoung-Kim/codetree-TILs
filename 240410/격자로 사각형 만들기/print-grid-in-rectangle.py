n = int(input())

nums=[]

for i in range(0,n):
    ith_num = []
    for j in range(0,n):
        if i == 0:
            ith_num.append(1)
        elif j == 0:
            ith_num.append(1)
        else:
            ith_num.append(nums[i-1][j]+ith_num[j-1])
    nums.append(ith_num)

print(nums)