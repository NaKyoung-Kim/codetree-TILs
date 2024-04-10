str_in = input()

result = []
cursor = 0

for s in str_in:
    if s == '-':
        del result[cursor-1]
    elif s == '>':
        if cursor < len(result):
            cursor += 1
    elif s == '<':
        if cursor > 0:
            cursor -= 1
    else:
        result.insert(cursor, s)
        cursor += 1

final = ''
for s in result:
    final += s
print(final)