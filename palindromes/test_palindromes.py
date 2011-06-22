#!/usr/bin/env python

import unittest

import palindromes

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assert_(palindromes.is_palindrome(''),
                     "Says the empty string isn't a palindrome.")


    def test_character_repetition(self):
        bees = ['b' * x for x in xrange(1,10) ]
        for b in bees:
            self.assert_(palindromes.is_palindrome(b),
                         "Says %d of the same character in a row isn't a palindrome" %
                         len(b))



if __name__ == '__main__':
    unittest.main()
    
