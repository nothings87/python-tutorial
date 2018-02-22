#!/usr/bin/env python3

import requests

URL = 'http://localhost:8000/cgi-bin/get.py'

# params={'lang': 'english',
#	'gender': 'male',
#	'company': 'yura'};

params={'name': 'eddie',
	'addr': 'uiwang',
	'lang': 'korean'};

print(">>>sending GET request with params");
response = requests.get(URL, params=params);

print(">>>status code");
print(response.status_code);

print("");
print(">>>response");
print(response.text);

