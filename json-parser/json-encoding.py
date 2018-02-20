import json

# Dictionary for test
cust = {
	'id': 152352,
	'name': 'jskang',
	'history': [
		{'date': '2015-03-11', 'item': 'iPhone'},
		{'date': '2014-11-23', 'item': 'Monitor'},
	]
}

# JSON Encoding

jsonString = json.dumps(cust);

print(jsonString);

print(type(jsonString));


