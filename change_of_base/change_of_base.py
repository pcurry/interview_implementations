#!/usr/bin/env python

CANONICAL_ORDER = '0123456789abcdefghijklmnopqrstuvwxyz_'


def validate_base(questionable_base):
    if questionable_base < 2 or questionable_base > len(CANONICAL_ORDER):
        raise ValueError("Base %s is invalid", questionable_base)

def int_to_string_in_base(value, target_base):
    validate_base(target_base)
    if value == 0:
        return '0'

    output = ''
    working = value
    while working > 0:
        digit = working % target_base
        output = CANONICAL_ORDER[digit] + output
        working = working / target_base
    return output


def int_from_string_with_base(number_string, source_base):
    validate_base(source_base)
    accum = 0
    for char in number_string.lower():
        accum = accum * source_base + CANONICAL_ORDER.index(char)
    return accum


def main():
    pass


def self_test():
    for x in xrange(1000):
        print "Number(base 10): %d" % x
        for y in CANONICAL_ORDER[2:]:
            base = CANONICAL_ORDER.index(y)
            string_value = int_to_string_in_base(x, base)
            print '\tBase: %d, String Representation: %s' % (base, string_value)
            assert x == int_from_string_with_base(string_value, base)
            round_trip = int_to_string_in_base(
                int_from_string_with_base(string_value, base),
                base)
            assert string_value == round_trip


if __name__ == '__main__':
    self_test()
