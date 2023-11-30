#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1

    if length == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(length, 's' if length > 1 else ''))

        for i in range(1, length + 1):
            print("{}: {}".format(i, argv[i]))
