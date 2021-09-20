# Write a Python function to Save a dictionary to a file
# Write a Python function to sort the words in a string
# INPUT: Dictionary to save,Output file path


# load function
# INPUT: DICT PATH
# OUTPUT: Return retrieved dictionary objet

# PICKLING: SERIALIZE THE PYTHON OBJECT TO A STRING
# UNPICKLING

import pickle


def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)


def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.pickle')
recovered = load_dict('test_dict.pickle')
print(recovered)



