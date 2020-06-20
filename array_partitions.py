

import doctest


def equal_sum(harry):
    """Given an array of positive integers, split the array in
    two sub-arrays (without reordering any elements) such that
    the sum of the first sub-array equals the sum of the
    second sub-array. Return the tuple of sub-arrays if
    such a split is found, or None if no such split is found.

    >>> equal_sum([]) is None
    True
    >>> equal_sum([5]) is None
    True
    >>> equal_sum([2, 3, 1]) is None
    True
    >>> equal_sum([1, 1])
    ([1], [1])
    """

    if len(harry) <= 1:
        return None

    beginning = 0
    end = len(harry) - 1  # higest index
    beginning_sum = harry[beginning]
    end_sum = harry[end]

    while beginning < end - 1:
        if beginning_sum > end_sum:
            end -= 1
            end_sum += harry[end]
        else:
            beginning += 1
            beginning_sum += harry[beginning]

    if beginning_sum == end_sum:
        return (harry[:end], harry[end:])
    else:
        return None


def equal_sum_recursive(harry, l_sum=None, r_sum=None):
    """This function should calculate the same results as the
    iterative version, equal_sum. This is a recursive
    implementation, primarily because I want to write one.

    """
    # First we handle the base cases
    if l_sum is None and r_sum is None:
        if not harry or len(harry) <= 1:
            return None
        if len(harry) == 2:
            if harry[0] == harry[1]:
                return (harry[0:1], harry[1:])
            else:
                return None

    # Now start handling the recursive cases



def equal_sum_tail_recursive(harry):
    pass
