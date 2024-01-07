#!/usr/bin/python3
""" Get the value of X-Request-Id in the header of the response """
from sys import argv
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
