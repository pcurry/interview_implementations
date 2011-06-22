#!/usr/bin/env python

import re

# Interview question about a palindrome detector function.
# I didn't finish the code on the board, and that annoyed me,
# so here we are.

def is_palindrome(in_str, including_spaces=False):
    """
    """
    if including_spaces:
        space_char = ' '
    else:
        space_char = ''
    cleanup_regex = str.format('[^a-zA-Z%s]+', space_char)
    de_punct = re.sub(cleanup_regex, '', in_str)
    working = de_punct.lower()
    front = 0
    back = len(working) - 1
    res = True
    while res and front <= back:
        res = res and working[front] == working[back]
        front += 1
        back -= 1
    return res

