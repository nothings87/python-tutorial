#!/usr/bin/env python3

import requests, json

URL = 'http://localhost:8000/cgi-bin/post_with_json.py'

data = {'name': 'Jaegwang Lee',
	'number': 'seven',
	'job': 'developer'};

# data=json.dumps(data)
response = requests.post(URL, data=json.dumps(data));

print(">>>status code");
print(response.status_code);

print("");
print(">>>response");
print(response.text);

