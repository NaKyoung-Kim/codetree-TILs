min_len = 21
max_len = -1

for _ in range(3):
    temp_len = len(input())
    max_len = temp_len if temp_len>max_len else max_len
    min_len = temp_len if temp_len<min_len else min_len
    
print(max_len - min_len)