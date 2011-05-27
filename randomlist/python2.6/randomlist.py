
from random import randrange

def random_list(ordered_list):
    elements = len(ordered_list)
    if elements == 1:
        return [ordered_list[0]]
    random_list = []
    for index in xrange(elements):
        working_length = elements - index 
        pick = randrange(working_length)
        random_list.append(ordered_list[pick])
        ordered_list[pick] = ordered_list[working_length - 1]
    return random_list