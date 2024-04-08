import sys
total = 0
count = 0

while 1:
    age = int(sys.stdin.readline())
    if age >= 30 or age < 20:
        print(format(total/count, ".2f"))
        break
    else:
        count += 1
        total += age