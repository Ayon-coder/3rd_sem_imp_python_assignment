bound = int(input("Enter the range: "))

for i in range(1, bound + 1):

    num = i
    sum = 0
    while(i > 0):

        rem = i % 10
        sum = sum*10 + rem
        i  = i // 10

    if(sum == num):
        print(f"{num} is palindrome number")