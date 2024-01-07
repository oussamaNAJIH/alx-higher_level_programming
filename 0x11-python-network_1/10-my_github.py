#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and personal access token as password)
and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    url = "https://api.github.com/user"

    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print(None)
