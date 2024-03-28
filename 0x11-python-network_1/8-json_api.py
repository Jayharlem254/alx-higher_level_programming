#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
response = requests.post(url, data={'q': q})

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

