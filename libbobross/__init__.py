#!/usr/bin/env python3

from os import path
import random
import textwrap

module_data = path.join(path.dirname(__file__), "data")
ascii_path = path.join(module_data, "ascii")
quotes_path = path.join(module_data, "quotes")

def build_bubble(quote=""):
    wrap_limit = 50
    wrap_list = textwrap.wrap(quote, wrap_limit)

    if len(wrap_list) == 1:
        wrap_limit = len(wrap_list[0])

    for i in range(len(wrap_list)):
        length_dif = wrap_limit - len(wrap_list[i])
        wrap_list[i] += (' ' * length_dif) + ' |'

    bubble = ' {0}\n| {1} |'
    for i in range(0, len(wrap_list)):
        bubble += '\n| {' + str(i + 2) + '}'
    bubble += '\n| {1} |\n {0}'
    return bubble.format("-" * (wrap_limit + 2), " " * wrap_limit, *wrap_list)


def main():
    with open(quotes_path, encoding='utf8') as quotes_file:
        print(build_bubble(random.choice(quotes_file.readlines())))

    with open(ascii_path) as ascii_file:
        print(ascii_file.read())
