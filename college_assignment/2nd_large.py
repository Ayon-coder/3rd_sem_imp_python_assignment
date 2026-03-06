num_list = list(map(int, input("Enter the number: ").split()))
max_num = max(num_list)
sec_max = float('-inf')

for i in range(len(num_list)):

    if num_list[i] > sec_max and num_list[i] < max_num:

        sec_max = num_list[i]

if sec_max == float('-inf'):
    print("No second largest number")
else:
    print(sec_max)