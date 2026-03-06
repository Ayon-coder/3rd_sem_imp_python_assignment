def num_list(num):

    num_list = []
    num = str(num)
    
    for i in num:
        num_list.append(int(i))
    
    return num_list

num = 21456
list1 = num_list(num)

while(len(list1) != 1):

    list1 = num_list(sum(list1))

if(list1[0] == 1):
    print("Magic number")
else:
    print("Not a magic number: ", list1[0])