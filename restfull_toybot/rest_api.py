#!/usr/bin/env python2.7

from webob import Request
from webob import Response
from webob import dec
from webob import exc


class RestfullToybot(object):

    def __call__(self, environ, start_response):
        req = Request(environ)
        if req.path_info_peek() == "list":
            return self.list(req)


    @dec.wsgify
    def list(self, req):
        resp = Response()
        

    def persist_bot(self, sessionid, toybot):
        pass

def main():
    app = RestfullToybot()
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', '5678', app)
    print 'Serving on http://localhost:5678'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C'


if __name__ == "__main__":
    main()
