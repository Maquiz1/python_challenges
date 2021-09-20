# Write a Python function to index all items in a list
# INPUT: list to search, value to search for
# OUTPUT: list of indices
# list can contain other list


def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices


example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# example = [1, 2, 3, 5, 2, 6, 9, 1]
print(index_all(example, 2))



