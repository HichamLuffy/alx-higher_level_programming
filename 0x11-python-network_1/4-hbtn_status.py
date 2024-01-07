#!/usr/bin/python3
""" HBTN Status """
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    data = res.text
    resquest_type = type(data)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(resquest_type, data))
