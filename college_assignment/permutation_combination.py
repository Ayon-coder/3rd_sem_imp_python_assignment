from itertools import combinations, permutations

num_list = input("Enter numbers by space: ").split()
r = int(input("Enter r: "))

print("\nCombination: ")

for c in combinations(num_list, r):
    print(c)

print("\npermutation: ")

for p in permutations(num_list, r):
    print(p)