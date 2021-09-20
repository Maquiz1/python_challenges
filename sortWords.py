# Write a Python function to sort the words in a string
# INPUT: STRING OF WORDS SEPARATED BY SPACES
# OUTPUT: STRING OF WORDS SORTED ALPHABETICALLY


def sort_words(inputs):
    words = inputs.split()                  # Break the string from each spaces
    words = [w.lower() + w for w in words]  # append lower case for each at the beginning
    words.sort()                            # sort the list
    words = [w[len(w)//2:] for w in words]  # take only the half
    return ' '.join(words)


print(sort_words('orange apple BANANA'))
