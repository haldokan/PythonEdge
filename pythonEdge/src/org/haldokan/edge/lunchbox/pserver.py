# server
#!C:\haldokan\3p\Python34\python.exe -u

import sys
import http.server
import urllib
from urllib import request

import cgi
import cgitb

cgitb.enable()  # for troubleshooting
"""
    By default this is a file server: 'http://localhost:8000' lists the files wher the server is run.
    Specifying a file name in the request gets the file content: 'http://localhost:8000/experiment.py'
"""
def runserver(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    # host = ''
    # or
    host = 'localhost'
    server_addr = (host, 8000)
    httpd = server_class(server_addr, handler_class)
    print('Runnig server on address: ' + repr(server_addr))
    httpd.serve_forever()

def runcgiserver(server_class=http.server.HTTPServer, handler_class=http.server.CGIHTTPRequestHandler):
    host = 'localhost'
    server_addr = (host, 8000)
    httpd = server_class(server_addr, handler_class)
    print('Runnig cgiserver on address: ' + repr(server_addr))
    httpd.serve_forever()

def runclient():
    try:
        with urllib.request.urlopen('http://localhost:8000/experiment.py') as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError:
        print('NOT FOUND')

def cgirequest():
    greetings = b'Hello there!'
    req = urllib.request.Request(url='http://localhost:8000/cgi-bin/test.cgi', data=greetings)
    f = urllib.request.urlopen(req)
    print(f.read().decode('utf-8S'))
    
def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print('Usage: pserver.py func')
        sys.exit(1)
        
    func = args[0]

    if func == '--runserver':
        runserver()
    if func == '--runcgiserver':
        runcgiserver()
    elif func == '--runclient':
        runclient()
    elif func == '--cgirequest':
        cgirequest()
    else: raise RuntimeError('function %s is not defined' % func)        
##
if __name__ == '__main__':
    main()
