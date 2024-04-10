def findNums(string):
    result=''
    for s in string:
        if s.isnumeric():
            result += s
    return int(result)

num1 = findNums(input())
num2 = findNums(input())

print(num1+num2)