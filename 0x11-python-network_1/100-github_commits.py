#!/usr/bin/python3
"""Module that takes your Github credentials (username and password) and uses
the Github API to display your id"""
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    json = response.json()
    for i in range(10):
        print("{}: {}".format(json[i].get('sha'), json[i].get('commit').get('author').get('name')))
        