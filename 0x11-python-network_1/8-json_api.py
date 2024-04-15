#!/usr/bin/python3
"""Module that takes in a letter and sends a POST request to
http://"""
import requests
from sys import argv
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(argv) > 1:
        q = argv[1]

    response = requests.post(url, data={'q': q})
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
