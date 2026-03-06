values = (11, [22, 33], 44, 55)

for i in values:
    if type(i) == list:
        print(len(i))
        for j in range(len(i)):
            pass
            if i[j] == 22:
                print('complete')
                i[j] = 222
print(values)
                