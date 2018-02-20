#!/usr/bin/env python3

import requests

URL = 'http://localhost:8000/cgi-bin/get.py'

print(">>>sending basic GET request");
response = requests.get(URL);

print(">>>status code");
print(response.status_code);

print("");
print(">>>response");
print(response.text);

