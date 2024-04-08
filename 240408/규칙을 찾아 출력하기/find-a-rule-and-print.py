n = int(input())

# for i in range(2*n-1):
#     for j in range(n):
#         if i % 2 != 0:
#             print(" ", end="")
#         elif j >= i:
#             print(" ", end="")
#         else:
#             print("*", end=" ")
#     print()


for j in range(n):
    for i in range(2*n):
        if i == 2*n-2:
            print("*", end="")
        elif i % 2 != 0:
            print(" ", end="")
        elif j == 0:
            print("*", end="")
        elif j*2-1 < i:
            print(" ", end="")
        else:
            print("*", end="")
            
    print()