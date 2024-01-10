#!/usr/bin/python3
"""
Module that returns an object (Python data structure) represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object(python data structure
    Args:
        my_str: python data structrep by the JSON string
    """
    return json.loads(my_str)
