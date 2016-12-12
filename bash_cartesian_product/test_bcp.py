#!/usr/bin/env python3

import unittest

import bcp


"""
a{b,c}d{e,f,g}hi

abdehi abdfhi abdghi acdehi acdfhi acdghi

a{b,c{d,e,f}g,h}ij{k,l}

abijk abijl acdgijk acdgijl acegijk acegijl acfgijk acfgijl ahijk ahijl
"""

class SimpleTests(unittest.TestCase):
    
    def test_empty_string(self):
        result = bcp.process_single_string("")
        self.assertEqual("", result)

    def test_plain_string(self):
        raw = "asdf"
        result = bcp.process_single_string(raw)
        self.assertEqual(raw, result)

    def test_complicated_string(self):
        raw = "a{b,c} d{e,f}"
        expected = "ab ac de df"
        result = bcp.process_string(raw)
        self.assertEqual(expected, result)
        
    def test_process_multiple_args(self):
        raw = ['f{e,i}e', 'f{o,um}']
        expected = "fee fie fo fum"
        result = bcp.process_args(raw)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
