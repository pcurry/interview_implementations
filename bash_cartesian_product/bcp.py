#!/usr/bin/env python3

import argparse

from collections import namedtuple

LiteralString = namedtuple("LiteralString", [value])

Product = namedtuple("Product", [components])



def process_string(raw):
    if raw == "":
        return ""
    if "{" not in raw and "}" not in raw and "," not in raw:
        return raw


def make_parser():
    pass


def main():
    parser = make_parser()
    products = process_string('foo')
    print(products)


if __name__ == '__main__':
    main()
