string = "I Purple you gojo edition"

string_list = string.split(" ")
cipher_string_list = []
for word in string_list:

    string = ""
    for letter in word:

        string += chr(ord(letter) + 1)
    
    cipher_string_list.append(string)
    string=""

print("Your cipher text is: ", " ".join(cipher_string_list))

normal_word_list = []
for word in cipher_string_list:

    string = ""
    for letter in word:

        string += chr(ord(letter) - 1)

    normal_word_list.append(string)
    string = ""

print("Your normal word is: ", " ".join(normal_word_list))