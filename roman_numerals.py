#!/usr/bin/env python2.7

"""
Write a method that converts its argument from integer to roman numeral if
a numeric value is passed, or from roman numeral to an integer if a roman
numeral is passed.  Your solution should rely on the parameter's class to
determine its type and if a non-roman numeral character is passed
(i.e. 'M3I',) the method should raise a BadRomanNumeral exception.

The solution should be a single method that accepts a single argument and
return the converted value.  Additionally, your solution should
demonstrate your mastery of Python's exception handling capabilities.

Include unit tests to verify correct conversion of both types of input,
and verify exception output with bad input.
"""

import re
import StringIO
import unittest

from collections import namedtuple


Equivalence = namedtuple("Equivalence", ["arabic", "roman"])


ARABIC_ROMAN_LIST = [
    Equivalence(roman="M", arabic=1000),
    Equivalence(roman="CM", arabic=900),
    Equivalence(roman="D", arabic=500),
    Equivalence(roman="CD", arabic=400),
    Equivalence(roman="C", arabic=100),
    Equivalence(roman="XC", arabic=90),
    Equivalence(roman="L", arabic=50),
    Equivalence(roman="XL", arabic=40),
    Equivalence(roman="X", arabic=10),
    Equivalence(roman="IX", arabic=9),
    Equivalence(roman="V", arabic=5),
    Equivalence(roman="IV", arabic=4),
    Equivalence(roman="I", arabic=1),
]


ROMAN_ARABIC_MAP = {
    equi.roman: equi.arabic for equi in ARABIC_ROMAN_LIST
}


VALID_ROMAN = r'^(M)*(CM|CD|D)?(C){0,4}(XC|XL|L)?(X){0,4}(IX|IV|V)?(I){0,4}$'
ROMAN_MATCHER = re.compile(VALID_ROMAN)


class BadRomanNumeral(ValueError):
    pass


def to_roman(number):
    if number < 1:
        raise BadRomanNumeral(number)

    roman_buffer = StringIO.StringIO()
    for equi in ARABIC_ROMAN_LIST:
        while number >= equi.arabic:
            roman_buffer.write(equi.roman)
            number = number - equi.arabic
    result = roman_buffer.getvalue()
    roman_buffer.close()
    return result


def to_arabic(numeral):
    if not ROMAN_MATCHER.match(numeral):
        raise BadRomanNumeral(numeral)
    result = 0
    position = 0

    while position < len(numeral):
        this_char = numeral[position]
        position = position + 1

        if this_char not in ROMAN_ARABIC_MAP:
            raise BadRomanNumeral(numeral)

        if position < len(numeral):
            pair = this_char + numeral[position]
            if pair in ROMAN_ARABIC_MAP:
                position = position + 1
                result = result + ROMAN_ARABIC_MAP[pair]
                continue

        result = result + ROMAN_ARABIC_MAP[this_char]

    return result


def arabic_roman_converter(value):
    if type(value) in (int, long):
        return to_roman(value)
    elif type(value) in (str, unicode):
        return to_arabic(value)
    else:
        raise BadRomanNumeral(value)


class TestArabicRomanConverter(unittest.TestCase):

    def roman_int_roundtrip(self, roman, int_val):
        self.assertEqual(roman, arabic_roman_converter(int_val))
        self.assertEqual(roman, arabic_roman_converter(long(int_val)))
        self.assertEqual(int_val, arabic_roman_converter(roman))
        self.assertEqual(
            int_val,
            arabic_roman_converter(arabic_roman_converter(int_val))
        )
        self.assertEqual(
            roman,
            arabic_roman_converter(arabic_roman_converter(roman))
        )

    def test_non_numeral_string(self):
        with self.assertRaises(BadRomanNumeral):
            arabic_roman_converter("froucerore")

    def test_malformed_numeral(self):
        with self.assertRaises(BadRomanNumeral):
            arabic_roman_converter("IXMC")

    def test_negative(self):
        with self.assertRaises(BadRomanNumeral):
            arabic_roman_converter(-1)

        with self.assertRaises(BadRomanNumeral):
            arabic_roman_converter(-1535)

    def test_zero(self):
        with self.assertRaises(BadRomanNumeral):
            to_roman(0)

    def test_one(self):
        self.roman_int_roundtrip("I", 1)

    def test_two(self):
        self.roman_int_roundtrip("II", 2)

    def test_three(self):
        self.roman_int_roundtrip("III", 3)

    def test_four(self):
        self.roman_int_roundtrip("IV", 4)

    def test_five(self):
        self.roman_int_roundtrip("V", 5)

    def test_six(self):
        self.roman_int_roundtrip("VI", 6)

    def test_nine(self):
        self.roman_int_roundtrip("IX", 9)

    def test_ten(self):
        self.roman_int_roundtrip("X", 10)

    def test_eleven(self):
        self.roman_int_roundtrip("XI", 11)

    def test_fourteen(self):
        self.roman_int_roundtrip("XIV", 14)

    def test_fifteen(self):
        self.roman_int_roundtrip("XV", 15)

    def test_sixteen(self):
        self.roman_int_roundtrip("XVI", 16)

    def test_nineteen(self):
        self.roman_int_roundtrip("XIX", 19)

    def test_twenty(self):
        self.roman_int_roundtrip("XX", 20)

    def test_fourty(self):
        self.roman_int_roundtrip("XL", 40)

    def test_fifty(self):
        self.roman_int_roundtrip("L", 50)

    def test_sixty(self):
        self.roman_int_roundtrip("LX", 60)

    def test_ninety(self):
        self.roman_int_roundtrip("XC", 90)

    def test_hundred(self):
        self.roman_int_roundtrip("C", 100)

    def test_four_hundred(self):
        self.roman_int_roundtrip("CD", 400)

    def test_five_hundred(self):
        self.roman_int_roundtrip("D", 500)

    def test_six_hundred(self):
        self.roman_int_roundtrip("DC", 600)

    def test_nine_hundred(self):
        self.roman_int_roundtrip("CM", 900)

    def test_thousand(self):
        self.roman_int_roundtrip("M", 1000)

    def test_eighteen_eighty_eight(self):
        self.roman_int_roundtrip("MDCCCLXXXVIII", 1888)

    def test_nineteen_ninety_nine(self):
        self.roman_int_roundtrip("MCMXCIX", 1999)


if __name__ == "__main__":
    unittest.main()
