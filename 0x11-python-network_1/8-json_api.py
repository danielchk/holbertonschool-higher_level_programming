#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    q = argv[1] if len(argv) > 1 else ""
    try:
        req = requests.post(url, data=data).json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req['id'], req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
