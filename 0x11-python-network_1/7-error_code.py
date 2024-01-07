#!/usr/bin/python3
""" displays the Error code"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
