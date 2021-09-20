# Write a Python function to count the number of unique words and how often each occurs
# INPUT: PATH TO A TEXT FILE
# OUTPUT: PRINT MESSAGE WITH
# TOTAL NUMBER OF WORDS
# TOP 10 MOST FREQUENT USED WORDS
# NUMBER OF OCCURRENCE FOR TOP 10


import re
from collections import Counter


def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print('\nTotal Words:', len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1

        print('\nTop 10 Words:')
        for word in word_counts.most_common(10):
            print(word[0], '\t', word[1])


count_words('text2.txt')