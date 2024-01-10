#!/usr/bin/python3
"""
Module to append string and return number of chars printed
"""


def append_write(filename="", text=""):
    """
    Apend a string and return no of chars appended
    Args:
        Filename: file to be appended
        text: str to append to file
    Returns: No of chars appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
