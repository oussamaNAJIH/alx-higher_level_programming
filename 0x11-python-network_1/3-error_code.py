#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
"""
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code:", e.code)
