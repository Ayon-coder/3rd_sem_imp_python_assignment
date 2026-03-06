hash_word = {}
word = "abcabcabc"

for i in word:

    hash_word[i] = hash_word.get(i, 0) + 1

word_list = []

for i, j in hash_word.items():

    if(j % 2 == 0):
       continue
    else:
        word_list.append(i)

print(''.join(word_list))