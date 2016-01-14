#!/usr/bin/env python2.7

from webob import Request
from webob import Response
from webob import dec
from webob import exc

from api_toybot import Robot


class RestfullToybot(object):

    def __init__(self):
        self.robots = {}

    @dec.wsgify
    def __call__(self, req):
        mount_point = req.path_info_pop()
        if req.method == "GET" and req.path_info_peek() == "list":
            return self.list(req)

        robot_name = req.path_info_pop()
        if req.method == "POST" and not req.path_info_peek():
            return self.create(robot_name)
        fail_default = Response()
        fail_default.status_int = 500
        return fail_default

    @dec.wsgify
    def create(self, robot_name):
        resp = Response()
        if robot_name in self.robots:
            resp.status_int = 303
        else:
            self.robots[robot_name] = Robot(robot_name)
        return resp

    @dec.wsgify
    def list(self, req):
        resp = Response()
        resp.content_type = 'application/json'
        # Get the robots
        resp.json = self.robots.keys()
        return resp


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
