#!/usr/bin/env python3

import requests

URL = 'http://localhost:3000/cgi-bin/post.cgi'

data = {'name': 'Jaegwang Lee',
	'number': 'seven',
	'job': 'developer'};

response = requests.post(URL, data=data);

print(">>>status code");
print(response.status_code);

print("");
print(">>>response");
print(response.text);

