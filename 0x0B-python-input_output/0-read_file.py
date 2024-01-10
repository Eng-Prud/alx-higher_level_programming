#!/usr/bin/python3
"""
Module for reading a text file(UTP8)and printing it to standard output
"""

def read_file(filename=""):
    """
    Reads file(UTF8)and prints it

    Args:
        filename(str): name of file being read

        Returns:
            None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())

if __name__ == "__main__":
    read_file()

