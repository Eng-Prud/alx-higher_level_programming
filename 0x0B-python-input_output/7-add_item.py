#!/usr/bin/python3
"""
Script for loading, adding, and saving items to a JSON file.
"""

import sys
from os.path import exists
from json import load, dump
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items from the file
items = load_from_json_file(filename)

# Add new items from command line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

