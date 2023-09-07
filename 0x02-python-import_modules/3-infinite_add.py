#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len = len(argv)-1
    x = 0
    if len >= 2:
        for i in range(1, len+1):
            x += int(argv[i])
        print("{:d}".format(x))
    else:
        print("{:d}".format(x))
