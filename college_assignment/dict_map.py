num_list = [10, 20, 30]
string_list = ['Ten', 'Twenty', 'Thirty']
map_dict = {}

for i, j  in zip(num_list, string_list):

    map_dict[j] = i

print(map_dict)