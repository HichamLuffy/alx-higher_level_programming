#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len = len(argv)-1
    if len == 0:
        print("0")
    x = 0
    for i in range(1, len+1):
        x += int(argv[i])
    print(x)
