#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable(display=0, logdir="./log")


form = cgi.FieldStorage()

if "name" not in form or "addr" not in form:
	print("<H1>Error</H1>");
	print("Please fill in the name and addr fields.");
	return;

print("name:", form["name"].value);
print("addr:", form["addr"].value);


