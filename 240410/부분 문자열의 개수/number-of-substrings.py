A = input()
B = input()

cnt = 0

for i in range(0, len(A)-1):
    if A[i] == B[0]:
        if A[i+1] == B[1]:
            cnt += 1
print(cnt)