#!/usr/bin/python3
""" My GitHub!"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    print(r.json().get('id'))
