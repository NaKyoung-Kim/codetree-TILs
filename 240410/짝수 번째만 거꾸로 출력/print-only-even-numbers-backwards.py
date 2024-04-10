str_in = input()

leng = len(str_in)
if leng % 2 != 0:
    str_in = str_in[:-1]
    leng -= 1

for i in range(leng-1, -1, -1):
    if i % 2 != 0:
        print(str_in[i], end="")