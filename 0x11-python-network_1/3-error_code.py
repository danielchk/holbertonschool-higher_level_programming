#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the body of the response"""

import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    """
    """
    info = {'email': argv[2]}
    data = urllib.parse.urlencode(info)
    data = data.encode('ascii')
    url = argv[1]
    reply = urllib.request.Request(url, data)
    with urllib.request.urlopen(reply) as rep:
        body = rep.read()
    print(body.decode(encoding="utf-8"))
