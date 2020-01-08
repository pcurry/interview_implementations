#!/usr/bin/env python3

"""

"""

import re

from collections import defaultdict


def string_stats(string):
    working, replacements_count = re.subn('[;:,. ]+', ' ', string)
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
    cow_sentence = "The cow jumped over the moon."
    commit_message = "Added the sentences library for an interview question."
    shortest_verse = "Jesus wept."
    assert(longest(cow_sentence) == "jumped")
    assert(shortest(cow_sentence) == "The")
    assert(longest(commit_message) == "sentences")
    assert(shortest(commit_message) == "an")
    assert(longest(shortest_verse) == "Jesus")
    assert(shortest(shortest_verse) == "wept")
