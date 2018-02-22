#!/usr/bin/env python3

import requests

URL = 'http://localhost:3000/cgi-bin/hello.cgi'

print(">>>sending basic GET request");
response = requests.get(URL);

print(">>>status code");
print(response.status_code);

print("");
print(">>>response.text");
print(response.text);

print(">>>response.headers");
print(response.headers);

