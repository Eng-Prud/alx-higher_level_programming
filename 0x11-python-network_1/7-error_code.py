#!/usr/bin/python3

# Handles HTTP errors.

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rv = requests.get(url)
    if rv.status_code >= 400:
        print("Error code: {}".format(rv.status_code))
    else:
        print(rv.text)
