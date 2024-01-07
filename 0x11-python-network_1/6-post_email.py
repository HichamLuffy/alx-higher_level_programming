#!/usr/bin/python3
""" Post an Email"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    res = requests.post(url, data=email)
    print(res.text)
