# Unfinished! Need to figure out a way to If two words score the same, return
# the word that appears earliest in the original string.

letter_dic = {'a': 1, 'b': 2,
              'c': 3, 'd': 4,
              'e': 5, 'f': 6,
              'g': 7, 'h': 8,
              'i': 9, 'j': 10,
              'k': 11, 'l': 12,
              'm': 13, 'n': 14,
              'o': 15, 'p': 16,
              'q': 17, 'r': 18,
              's': 19, 't': 20,
              'u': 21, 'v': 22,
              'w': 23, 'x': 24,
              'y': 25, 'z': 26}

words = 'd bb'
sum_list = []
for word in words.split():
    chars = list(word)
    suma = 0
    for i in chars:
        suma += letter_dic[i]
    sum_list.append(suma)

word_dict = dict(zip(sum_list, words.split()))
sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[0], reverse=True)
result = (sorted_word_dict[0])
print(result[1])
