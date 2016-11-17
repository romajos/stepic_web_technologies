# -*- coding: utf-8 -*-
#!/usr/bin/python3

def wsgi_application(environ, start_response):
    data = [(x + '\n').encode() for x in environ['QUERY_STRING'].split('&')]
    #print(data)
    start_response("200 OK", [("Content-Type", "text/plain")])
    return data