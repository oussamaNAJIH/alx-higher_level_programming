#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1]:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {"q": letter}
    r = requests.post(url, data=data)
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
