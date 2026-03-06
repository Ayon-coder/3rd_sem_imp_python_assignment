letter_ascii_dict = {}

for i in range(26):

    letter_ascii_dict[chr(i + 97)] = i + 1

letter_input = "aaa"
num = 0
for i in range(len(letter_input)):

    num += letter_ascii_dict.get(letter_input[i], 0)

if(num == len(letter_input)):

    print("It is fucking super Ascii")