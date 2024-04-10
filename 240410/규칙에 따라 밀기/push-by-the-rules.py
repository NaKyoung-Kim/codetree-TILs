str_in = input()
command = input()

LorR = 0

for c in command:
    if c == 'L':
        LorR += 1
    else:
        LorR -= 1

if LorR > 0:
    move = str_in[:LorR]
    str_in = str_in[LorR:]+move
elif LorR < 0:
    move = str_in[LorR:]
    str_in = move+str_in[:LorR]

print(str_in)