# Write a Python function to PASSPHRASES
# INPUT: NUMBER OF WORDS IN PASSPHRASES
# OUTPUT: STRING OF RANDOM WORDS ,SEPARATED BY SPACES


import secrets


def gen_pass(num_words):
    with open('text2.txt', 'r') as file:
        lines = file.readlines()[4:5]
        words_list = [line.split()[1] for line in lines]

    words = [secrets.choice(words_list) for i in range(num_words)]
    return ' '.join(words)


gen_pass(4)