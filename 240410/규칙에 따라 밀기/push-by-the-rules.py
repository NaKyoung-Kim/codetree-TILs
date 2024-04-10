str_in = input()
command = input()

total_len = len(str_in)
LorR = 0

for c in command:
    if c == 'L':
        LorR += 1
    else:
        LorR -= 1

if LorR >= total_len:
    while LorR > total_len:
        LorR -= total_len
elif LorR <= -(total_len):
    while LorR < -total_len:
        LorR += total_len

if LorR > 0:
    move = str_in[:LorR]
    str_in = str_in[LorR:]+move
elif LorR < 0:
    move = str_in[LorR:]
    str_in = move+str_in[:LorR]

print(str_in)