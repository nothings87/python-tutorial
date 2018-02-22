#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

server = BaseHTTPServer.HTTPServer;
handler = CGIHTTPServer.CGIHTTPRequestHandler;

server_addr = ("", 8000);
# handler.cgi_directories = ["/"];

httpd = server(server_addr, handler)
httpd.serve_forever()

