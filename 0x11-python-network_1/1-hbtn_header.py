#!/usr/bin/python3
"""script that takes
in a url sends a request to the URL
and displays the value of the X-Request-Id Variable found in the header
of the response"""


import urllib.request
from sys import argv
if __name__ == "__main__":
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')

    print(header)
