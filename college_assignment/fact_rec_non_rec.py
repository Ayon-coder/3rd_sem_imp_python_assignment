# def recursion(n):

#     if(n == 1):
#         return 1
#     return n * recursion(n - 1)

# print(recursion(5))

def fact(n):

    res = 1

    while(n != 0):

        res = res * (n)
        n -= 1
    
    return res

print(fact(5))