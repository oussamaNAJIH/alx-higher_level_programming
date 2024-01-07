#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url)
    try:
        print(r.text)
    except requests.exceptions.RequestException:
        print(r.status_code)
