#!/usr/bin/python3
"""appden after a string"""


def append_after(filename="", search_string="", new_string=""):
    """appden after a string"""
    with open(filename, "r") as f:
        text = f.read()
    text = text.replace(search_string, new_string)
    with open(filename, "w") as f:
        f.write(text)
