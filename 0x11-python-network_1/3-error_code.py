#!/usr/bin/python3
"""script that takes in a url sends a request to the url
and displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
