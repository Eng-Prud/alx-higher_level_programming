#!/usr/bin/python3
# using the urlib packages
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as ress:
        b = ress.read()
        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
