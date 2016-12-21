#!/usr/bin/env python3

"""
This is p
"""

import argparse

from collections import namedtuple


LiteralString = namedtuple("LiteralString", ["value"])


Product = namedtuple("Product", ["sets"])


def is_simple_string(raw):
    if raw == "":
        return True
    if "{" not in raw and "}" not in raw and "," not in raw and " " not in raw:
        return True
    return False


def parse_string(raw):
    start_literal = 0
    subunits = []
    components = []

    current = 0
    total_consumed = 0

    def record_literal_if_needed(end_literal):
        if end_literal > start_literal:
            components.append(LiteralString(raw[start_literal:end_literal]))

    while current < len(raw):
        if raw[current] == " ":
            record_literal_if_needed(current)
            subunits.append(components[:])
            components.clear()
            next_char = current + 1
            start_literal = next_char
            current = next_char
        elif raw[current] == "\\":
            record_literal_if_needed(current)
            start_literal = current + 1
            current = current + 2
        elif raw[current] == "{":
            record_literal_if_needed(current)
            parsed_product, consumed = parse_product(raw[current:])
            components.append(parsed_product)
            next_char = current + consumed
            start_literal = next_char
            current = next_char
        elif raw[current] in ("}", ","):
            break
        else:
            current = current + 1

    record_literal_if_needed(current)

    return components, subunits, current


def process_string(raw):
    if is_simple_string(raw):
        return raw

    if " " in raw and "\ " not in raw:
        return process_list_of_strings(raw.split())

    components, subunits, consumed = parse_string(raw)
    print(consumed)
    print(len(raw))

    rendered_components = " ".join(render(components))

    if subunits:
        rendered_subunits = [" ".join(render(subunit)) for subunit in subunits]
        if rendered_components:
            rendered_subunits.append(rendered_components)
        return " ".join(rendered_subunits)
    else:
        return rendered_components


def parse_product(raw):
    if '}' not in raw:
        return LiteralString(raw), len(raw)

    total_consumed = 0
    starting_point = 1
    components = []

    while True:
        next_substring = raw[starting_point:]
        new_components, subunits, consumed = parse_string(next_substring)

        if subunits:
            raise ValueError("Should not be unescaped spaces in products")

        if consumed >= len(next_substring):
            final_components = []
            for component in components:
                final_components.append(component)
                final_components.append(LiteralString(","))
            for component in new_components[:-1]:
                final_components.append(component)
                final_components.append(LiteralString(","))
            final_components.append(new_components[-1])
            final_components.append(LiteralString(next_substring[-1]))
            return Product(final_components), len(raw)

        total_consumed = starting_point + consumed
        if raw[total_consumed] == "}":
            if len(components) + len(new_components) == 1:
                return Product([
                    LiteralString("{"),
                    (components + new_components)[0],
                    LiteralString("}")
                ]), total_consumed
            else:
                components.append(Product(new_components))
                return Product(components), total_consumed
        else:
            components.append(Product(new_components))
            starting_point = total_consumed + 1


def process_list_of_strings(args):
    processed_strings = [process_string(arg) for arg in args]
    return " ".join(processed_strings)


def render(components):
    results = [""]
    for component in components:
        if type(component) == LiteralString:
            results = [result + component.value for result in results]
        elif type(component) == Product:
            results = [
                result + image
                for result in results
                for image in render(component.sets)
            ]
        elif type(component) == list:
            rendered_subunits = render(component)
            results = [
                result + subunit
                for result in results
                for subunit in rendered_subunits
            ]
        else:
            raise ValueError(component)
    return results


# The following functions are for running this library as a script.

def make_args_parser():
    parser = argparse.ArgumentParser(
        description="Consumes strings from command input to turn into bash products."
    )
    parser.add_argument(
        "substrings",
        metavar="S",
        type=str,
        nargs="+",
        help="a string to process"
    )
    return parser


def main():
    parser = make_args_parser()
    args = parser.parseargs()
    products = process_list_of_strings(args)
    print(products)


if __name__ == "__main__":
    main()
