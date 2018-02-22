#!/usr/bin/env python3

from os import path
import random

module_data = path.join(path.dirname(__file__), "data")
ascii_path = path.join(module_data, "ascii")
quotes_path = path.join(module_data, "quotes")

bubble = """
 {0}
| {1} |
| {2} |
| {1} |
 {0}
""".rstrip()

def build_bubble(quote=""):
    return bubble.format("-" * (len(quote) + 1), " " * (len(quote) - 1),
                         quote.strip())


def main():
 
    with open(quotes_path) as quotes_file:
        print(build_bubble(random.choice(quotes_file.readlines())))

    with open(ascii_path) as ascii_file:
        print(ascii_file.read())
