#!/usr/bin/env python3

"""
Functions to count various features of ordered lists of integers
"""


import itertools

from collections import Counter


def arbitrary_difference(numbers, difference):
    """
    Given a list of numbers and a value of a difference between a pair of
    numbers chosen from the list, return the set of distinct pairs.
    """



def equal_adjacent_pairs(numbers):
    """
    Given a sequence of numbers, return a count of the number of times
    the subsequence (x, x) occurs in the sequence.
    """

    count = Counter()
    for i in range(len(numbers)):
        current = numbers[i]
        if current == numbers[i + 1]:
            count[(current, current)] += 1
    return count
