lwr = input()
num = ord(lwr)
if num == 97:
    num = 122
else:
    num -= 1

print(chr(num))