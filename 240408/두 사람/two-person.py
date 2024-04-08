peoples = []
peoples.append(list(input().split()))
peoples.append((input().split()))
flag = 0

for i in range(2):
    if int(peoples[i][0]) >= 19 and peoples[i][1] == 'M':
        flag = 1
        break
        
print(flag)