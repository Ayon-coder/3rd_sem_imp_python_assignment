num_list = [1, 1, 2, 2, 3, 3]

seen = set()

first_list = []
last_list = []

for i in num_list:
    if i in seen:
        last_list.append(i)
    else:
        seen.add(i)

print(list(seen) + last_list)