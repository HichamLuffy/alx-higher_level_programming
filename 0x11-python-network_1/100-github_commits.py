#!/usr/bin/python3
""" Time for an interview!"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits?per_page={}'
    url = url.format(
        argv[2], argv[1], 10
    )
    r = requests.get(url)
    commits = r.json()
    for c in commits:
        print("{}: {}"
              .format(c.get('sha'), c.get('commit').get('author').get('name')))
