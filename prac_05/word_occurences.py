"""
CP1404 | Prac_05 | Dannielle Jones
Count the occurrences of words in a string.
"""

word_to_count = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
words = sorted(word_to_count, key=word_to_count.get(0))
max_length = max([len(word[0]) for word in words])
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
