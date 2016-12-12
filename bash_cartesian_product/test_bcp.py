#!/usr/bin/env python3

import unittest

import bcp


class ProcessingTests(unittest.TestCase):
    
    def test_example_one(self):
        raw = "a{b,c}d{e,f,g}hi"
        expected = "abdehi abdfhi abdghi acdehi acdfhi acdghi"
        result = bcp.process_string(raw)
        self.assertEqual(expected, result)

    def test_example_two(self):
        raw = "a{b,c{d,e,f}g,h}ij{k,l}"
        expected = "abijk abijl acdgijk acdgijl acegijk acegijl acfgijk acfgijl ahijk ahijl"
        result = bcp.process_string(raw)
        self.assertEqual(expected, result)

    def test_empty_string(self):
        result = bcp.process_string("")
        self.assertEqual("", result)

    def test_plain_string(self):
        raw = "asdf"
        result = bcp.process_string(raw)
        self.assertEqual(raw, result)

    def test_unescaped_spaces(self):
        raw = "a{b,c} d{e,f}"
        expected = "ab ac de df"
        result = bcp.process_string(raw)
        self.assertEqual(expected, result)
        
    def test_escaped_spaces(self):
        raw = "a{b,c}\ d{e,f}"
        expected = "ab de ab df ac de ac df"
        result = bcp.process_string(raw)
        self.assertEqual(expected, result)
    
    def test_process_multiple_args(self):
        raw = ['f{e,i}e', 'f{o,um}']
        expected = "fee fie fo fum"
        result = bcp.process_list_of_strings(raw)
        self.assertEqual(expected, result)

    def test_literal_curly_braces(self):
        just_braces = "a{bc}"
        just_braces_result = bcp.process_string(just_braces)
        self.assertEqual(just_braces, just_braces_result)
        unclosed_brace = "a{b,c"
        unclosed_brace_result = bcp.process_string(unclosed_brace)
        self.assertEqual(unclosed_brace, unclosed_brace_result)

    def test_product_escape_sequences(self):
        escaped_braces = "a\{b,c\}"
        escaped_comma = "a{b\,c}"
        escaped_expected = "a{b,c}"
        escaped_braces_result = bcp.process_string(escaped_braces)
        self.assertEqual(escaped_expected, escaped_braces_result)
        escaped_comma_result = bcp.process_string(escaped_comma)
        self.assertEqual(escaped_expected, escaped_comma_result)
        

if __name__ == "__main__":
    unittest.main()
