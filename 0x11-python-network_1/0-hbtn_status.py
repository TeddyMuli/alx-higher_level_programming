#!/usr/bin/python3
"""script to fetch url"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    b_bytes = response.read()
    b_str = b_bytes.decode('utf-8')

print("Body response:")
print("\t- type:", type(b_bytes))
print("\t- content:", b_bytes)
print("\t- utf8 content:", b_str)
