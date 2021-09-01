"""
CP1404 | Prac_05 | Dannielle Jones
Count the occurrences of words in a string.
"""
from operator import itemgetter

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
word_to_count_list = [(word, count) for word, count in word_to_count.items()]
word_to_count_list.sort(key=itemgetter(0))
longest_word = max([len(word[0]) for word in word_to_count_list])
for word, count in word_to_count_list:
    print("{:{}} : {}".format(word, longest_word, count))





