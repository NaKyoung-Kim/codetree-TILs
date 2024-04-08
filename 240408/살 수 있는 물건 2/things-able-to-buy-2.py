stuff_list = ["book", "mask", "pen", "no"]
price_list = [3000, 1000, 500, 0]

n = int(input())

for i in range(len(price_list)):
    if n >= price_list[i]:
        print(stuff_list[i])
    break