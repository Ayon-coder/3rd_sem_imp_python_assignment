dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merged = {**dict_1}

for i, j in dict_2.items():

    if j not in merged.values():

        merged[i] = j

print(merged)