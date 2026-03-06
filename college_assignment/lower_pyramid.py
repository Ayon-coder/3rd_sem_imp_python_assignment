bound = l = 11

for i in range(1, bound + 1):

    for k in range(i):
        print(" ", end = ' ')
    for j in range(2 * l - 1):
        print("*", end = ' ')
    
    print()
    l -= 1