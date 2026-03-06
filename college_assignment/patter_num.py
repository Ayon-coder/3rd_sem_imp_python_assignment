# bound = 5

# for i in range(1, bound + 1):

#     for k in range(bound - i):
#         print("   ", end="")   # 3 spaces for alignment

#     for j in range(1, i + 1):
#         print(j, end="   ")    # same spacing

#     print()

bound = 7

for i in range(1, bound + 1):

    for k in range(bound - i):
        print("  ", end="")   # leading spaces

    for j in range(1, i + 1):
        print(j, end="   ")   # numbers

    print()

for i in range(bound, 0, -1):

    for k in range(bound - (i - 1)):
        print("  ", end = "")
    for j in range(1, i):
        print(j, end = "   ");
    print()