"""
CP1404 - Work Occurrences
Estimate: 15 min
Actual: 10 min
"""

text = "this is a collection of words of nice words this is a fun thing it is"

# text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
words = [word for word in word_to_count]
words.sort()
width = max([len(word) for word in words])
for word in words:
    print(f"{word:>{width}} : {word_to_count[word]}")
