#!/usr/bin/python3
"""
Module that writes an object to a text file, using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation
    Args:
        my_obj: object to be saved
        filename: name of file to save the object to
    Returns:
    None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
