#!/usr/bin/env python3

"""

"""

import re
import unittest

from collections import defaultdict


def string_stats(string):
    if string is None:
        raise ValueError("Expected a string, got a None")

    working, dash_replacements = re.subn(' [-]+ ', ' ', string)
    working, replacements_count = re.subn('[;:,.=>< ]+', ' ', working)
    just_words = working.strip()

    if len(just_words) == 0:
        return '', '', {0: []}

    counts = defaultdict(list)

    for word in just_words.split(' '):
        counts[len(word)].append(word)

    lengths = sorted(list(counts.keys()))
    shortest = counts[lengths[0]][0]
    longest = counts[lengths[-1]][0]
    return shortest, longest, counts


def longest(string):
    shortest, longest, counts = string_stats(string)
    return longest, len(longest)


def shortest(string):
    shortest, longest, counts = string_stats(string)
    return shortest, len(shortest)



class TestStringStats(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(ValueError):
            string_stats(None)

    def test_empty_string(self):
        least, most, counts = string_stats('')
        self.assertEqual(least, '')
        self.assertEqual(most, '')
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0], [])

    def test_period(self):
        least, most, counts = string_stats('.')
        self.assertEqual(least, '')
        self.assertEqual(most, '')
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0], [])

    def test_semicolon(self):
        least, most, counts = string_stats('; ')
        self.assertEqual(least, '')
        self.assertEqual(most, '')
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0], [])

    def test_ellipsis(self):
        least, most, counts = string_stats(' ... ')
        self.assertEqual(least, '')
        self.assertEqual(most, '')
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0], [])

    def test_dash(self):
        least, most, counts = string_stats('b --- aa')
        self.assertEqual(least, 'b')
        self.assertEqual(most, 'aa')
        self.assertEqual(len(counts), 2)
        self.assertEqual(counts[1], ['b'])
        self.assertEqual(counts[2], ['aa'])

    def test_cow_sentence(self):
        cow_sentence = "The cow jumped over the moon."
        least, most, counts = string_stats(cow_sentence)
        self.assertEqual(least, "The")
        self.assertEqual(most, "jumped")

    def test_commit_message(self):
        commit_message = "Added the sentences library for an interview question."
        least, most, counts = string_stats(commit_message)
        self.assertEqual(least, "an")
        self.assertEqual(most, "sentences")

    def test_shortest_verse(self):
        shortest_verse = "Jesus wept."
        least, most, counts = string_stats(shortest_verse)
        self.assertEqual(least, "wept")
        self.assertEqual(most, "Jesus")


class TestLongest(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(ValueError):
            longest(None)

    def test_empty_string(self):
        self.assertEqual(longest(''), ('', 0))

    def test_cow_sentence(self):
        cow_sentence = "The cow jumped over the moon."
        self.assertEqual(longest(cow_sentence), ("jumped", 6))

    def test_commit_message(self):
        commit_message = "Added the sentences library for an interview question."
        self.assertEqual(longest(commit_message), ("sentences", 9))

    def test_shortest_verse(self):
        shortest_verse = "Jesus wept."
        self.assertEqual(longest(shortest_verse), ("Jesus", 5))


class TestShortest(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(ValueError):
            shortest(None)

    def test_empty_string(self):
        self.assertEqual(shortest(''), ('', 0))

    def test_cow_sentence(self):
        cow_sentence = "The cow jumped over the moon."
        self.assertEqual(shortest(cow_sentence), ("The", 3))

    def test_commit_message(self):
        commit_message = "Added the sentences library for an interview question."
        self.assertEqual(shortest(commit_message), ("an", 2))

    def test_shortest_verse(self):
        shortest_verse = "Jesus wept."
        self.assertEqual(shortest(shortest_verse), ("wept", 4))



if __name__ == '__main__':
    print("Testing sentences library")
    unittest.main()
