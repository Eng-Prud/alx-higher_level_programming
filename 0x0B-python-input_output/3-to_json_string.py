#!/usr/bin/python3
"""
Module that returns JSON rep of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON rep of an object
    Args:
        my_obj: object to be converted to a JSON string
    """
    return json.dumps(my_obj)
