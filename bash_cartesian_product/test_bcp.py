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
        result = bcp.product("")
        self.assertEquals("", result)

    def test_plain_string(self):
        

if __name__ == "__main__":
    unittest.main()
