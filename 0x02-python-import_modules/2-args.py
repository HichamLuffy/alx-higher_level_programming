#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    len = len(argv)-1
    if (len == 0):
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format(len))
    for i in range(1, len+1, 1):
        print("{}: {}".format(i, argv[i]))
