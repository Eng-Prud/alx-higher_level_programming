#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a str to a text file
    Args:
        Filename(str): Name of file to write
        text(str):str to write to file
    Returns:
        int: no of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
