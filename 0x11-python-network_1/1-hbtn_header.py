#!/usr/bin/python3
"""
displays the value of the X-Request-Id
"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    Id = response.getheader("X-Request-Id")
    print(Id)
