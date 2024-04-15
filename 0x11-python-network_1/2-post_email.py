#!/usr/bin/python3
""" a script that takes a url
and an email, sends a post request
to the url, display the body of the response"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')

    print(body)
