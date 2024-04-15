#!/usr/bin/python3
"""Write a Python script that fetches
https://alx-intranet.hbtn.io/status"""


import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
else:
    print("Error code: ", response.status_code)
    