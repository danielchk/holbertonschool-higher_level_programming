#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv
if __name__ == '__main__':
    if len(argv) == 2:
        req = argv[1]
    else:
        req = ""
    postr = requests.post('http://0.0.0.0:5000/search_user', data={'req': req})
    try:
        jsondic = postr.json()
        id = jsondic.get('id')
        name = jsondic.get('name')
        if len(jsondic) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(jsondic.get('id'), jsondic.get('name')))
    except:
        print("Not a valid JSON")
