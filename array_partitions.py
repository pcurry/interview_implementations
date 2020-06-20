

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
    # First we handle first call cases
    if l_sum is None and r_sum is None:
        if len(harry) == 2:
            if harry[0] == harry[1]:
                return ([harry[0]], [harry[1]])
            else:
                return None
        if not harry or len(harry) <= 1:
            return None
        else:
            lhv = harry[0]
            rhv = harry[-1]
            recursed = equal_sum_recursive(harry[1:-1], lhv, rhv)
            if recursed is None:
                return None
            else:
                return ([lhv] + recursed[0], recursed[1] + [rhv])

    # Now start handling the recursive cases
    if len(harry) == 0:
        return ([], [])

    if l_sum > r_sum:
        rhv = harry[-1]
        recurse = equal_sum_recursive(harry[:-1], l_sum, r_sum + rhv)
        if recurse is None:
            return None
        else:
            return (recurse[0], recurse[1] + [rhv])
    else:
        lhv = harry[0]
        recurse = equal_sum_recursive(harry[1:], l_sum + lhv, r_sum)
        if recurse is None:
            return None
        else:
            return ([lhv] + recurse[0], recurse[1])

    raise Exception()


def equal_sum_tail_recursive(harry, l_sum=None, l_array=None, r_sum=None, r_array=None):
    pass
