
from random import randrange, randint

def randomize_list_append(ordered_list):
    """ Expects an ordered list of at least two elements. 
    Returns a new list, composed of the elements of the source list, 
    in random order.
    Modifies the ordered_list as a side effect of generating a random list.
    """
    choices = len(ordered_list) - 1
    random_list = []
    while choices > 0:
        pick = randint(0, choices)
        temp = ordered_list[pick]
        random_list.append(temp)
        ordered_list[pick] = ordered_list[choices]
        ordered_list[choices] = temp
        choices -= 1
    random_list.append(ordered_list[0])
    return random_list


def randomize_list_insert(ordered_list):
    """ Expects an ordered list of at least two elements. 
    """
    elements = len(ordered_list)
    random_list = [x for x in xrange(elements)]
    choices = elements - 1
    for idx in xrange(choices):
        pick = randint(idx, choices)
        temp = ordered_list[pick]
        random_list[idx] = temp
        if pick != idx:
            ordered_list[pick] = ordered_list[idx]
            ordered_list[idx] = temp
    random_list[choices] = ordered_list[choices]
    return random_list

def randomize_list_comprehension(ordered_list):
    """ Expects an ordered list of at least two elements. 
    """
    def swap_pop(lyst, index):
        value = lyst.pop()
        if index < len(lyst):
            lyst[index] = value
    choices = len(ordered_list) - 1
    indices = [randint(0, x) for x in xrange(choices, -1, -1)]    
    return [(ordered_list[y], swap_pop(ordered_list, y))[0] for y in indices]

def randomize_list_in_place(ordered_list):
    """ Takes an ordered list.  Randomizes it in place.
    """
    elements = len(ordered_list)
    while elements > 0:
        pick = randrange(elements)
        elements = elements - 1
        temp = ordered_list[pick]
        ordered_list[pick] = ordered_list[elements]
        ordered_list[elements] = temp


def random_list(ordered_seq, randomizing_method=randomize_list_append):
    """ Accepts an ordered sequence.  

    Returns a list containing the elements of that sequence in random order.
    """
    elements = len(ordered_seq)
    if ordered_seq in ([], (), set([])) or elements == 0:
        return []
    elif elements == 1:
        return [ordered_seq[0]]
    else:
        return randomizing_method(list(ordered_seq))
