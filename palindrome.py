# Write a Python function to determine if a given string is a palindrome
# Palindrome is Word or phrase that reads the same forwards as backwards e.g level,race car
# INPUT: STRING TO VALUE
# OUTPUT: BOOLEAN VALUE
# ONLY CONSIDER LETTERS(A - Z)
# IGNORE CASE (FOR EXAMPLE , 'A' == 'a')

import re


def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(is_palindrome('Go hang a salami - I\'m a lasagna hog'))
