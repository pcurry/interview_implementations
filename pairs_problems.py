#!/usr/bin/env python3

"""
Functions to count various features of lists of integers
"""


import itertools

from collections import Counter
from collections import defaultdict

def arbitrary_difference(numbers, difference):
    """
    Given a list of numbers and a value of a difference between a pair of
    numbers chosen from the list, return the nuumber distinct pairs that satisfy
    this difference.
    """
    count = Counter(numbers)
    pairs = set((a, a + difference) for a in count.keys() if count[a + difference] > 0)
    return len(pairs)


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


def title_pairs_for_runtime(playtimes, runtime):
    mod_times = defaultdict(list)
    for i in range(len(playtimes)):
        mod_times[playtimes[i] % runtime].append(i)
    title_pairs = set()
    for mt in mod_times.keys():
        if mod_times[runtime - mt]:
            for x in mod_times[mt]:
                for y in mod_times[runtime - mt]:
                    title_pairs.add((x, y))
    if len(mod_times[0]) > 1:
        even_length = mod_times[0]
        for a in even_length:
            for b in even_length:
                if a != b:
                    title_pairs.add((a, b))
    return len(title_pairs)
