#!/usr/bin/python3
"""Defines a peak."""


def find_peak(n):
    """ Finds the peak in a list of integers """
    if n == []:
        return None

    length = len(n)
    m = int(length / 2)
    li = n

    if m - 1 < 0 and m + 1 >= length:
        return li[m]
    elif m - 1 < 0:
        return li[m] if li[m] > li[m + 1] else li[m + 1]
    elif m + 1 >= length:
        return li[m] if li[m] > li[m - 1] else li[m - 1]

    if li[m - 1] < li[m] > li[m + 1]:
        return li[m]

    if li[m + 1] > li[m - 1]:
        return find_peak(li[m:])
    return find_peak(li[:m])
