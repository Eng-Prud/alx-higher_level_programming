#!/usr/bin/python3
"""
Module to create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Create an onject from a JSON file
    Args:
        filename: name of JSON file
    Returns:
        obj: the python data struct rep by JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
