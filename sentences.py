#!/usr/bin/env python3

"""

"""

import re

from collections import defaultdict


def string_stats(string):
    working, replacements_count = re.subn('[;:,.]+', ' ', string)
    words = working.strip().split(' ')
    counts = defaultdict(list)
    for word in words:
        counts[len(word)].append(word)

    lengths = sorted(list(counts.keys()))
    shortest = counts[lengths[0]][0]
    longest = counts[lengths[-1]][0]
    return shortest, longest, counts


def longest(string):
    shortest, longest, counts = string_stats(string)
    return longest


def shortest(string):
    shortest, longest, counts = string_stats(string)
    return shortest


if __name__ == '__main__':
    print("Testing sentences library")
    
