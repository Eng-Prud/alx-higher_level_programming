#!/usr/bin/python3

for p in range(10):
    for q in range(p + 1, 10):
        print("{:d}{:d}".format(p, q), end=", ")
print()
