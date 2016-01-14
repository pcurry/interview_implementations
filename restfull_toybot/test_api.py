#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import unittest

from webob import Request
from webob import Response
from webob import exc

from webtest import TestApp

from rest_api import RestfullToybot


class TestAPI(unittest.TestCase):

    def setUp(self):
        # Make API app
        super(TestAPI, self).setUp()
        self.app = TestApp(RestfullToybot())

    def tearDown(self):
        # Clean up mess
        del self.app
        super(TestAPI, self).tearDown()

    def test_create_bot(self):
        resp = self.app.post("/robot/danherr")
        resp2 = self.app.get("/robot/danherr")

        # Some more stuff to validate having a functional bot.

    def test_create_bot_collision(self):
        resp = self.app.post("/robot/alec")
        resp2 = self.app.post("/robot/alec")
        self.assertEqual(303, resp2.status_int)

    def test_list_bots_none(self):
        resp = self.app.get("/robot/list")
        self.assertEqual([], resp.json)

    def test_list_bots_some(self):
        create_dan = self.app.post("/robot/danherr")
        robots = self.app.get("/robot/list")
        self.assertEqual(["danherr"], robots.json)

        create_alec = self.app.post("/robot/alec")
        robots = self.app.get("/robot/list")
        robots_list = list(robots.json)
        self.assertIn("alec", robots_list)
        self.assertIn("danherr", robots_list)


        """
        app = TestApp(application)
Then you can get the response of a HTTP GET:

>>> resp = app.get('/')
And check the results, like response’s status:

>>> assert resp.status == '200 OK'
>>> assert resp.status_int == 200
Response’s headers:

>>> assert resp.content_type == 'text/html'
>>> assert resp.content_length > 0
Or response’s body:
"""


"""
Input and Output:

a)----------------

PLACE 0,0, NORTH
MOVE
REPORT Output: 0,1,NORTH

b)----------------

PLACE 0,0,NORTH
LEFT
REPORT Output: 0,0,WEST

c)----------------

PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT Output: 3,3,NORTH
"""
    ## def test_create_bot(self):
    ##     self.assertTrue(False)

    ## def test_recreate_bot(self):
    ##     self.assertTrue(False)

    ## def test_place_bot(self):
    ##     self.assertTrue(False)

    ## def test_replace_bot(self):
    ##     self.assertTrue(False)

    ## def test_change_right(self):
    ##     self.assertTrue(False)

    ## def test_change_left(self):
    ##     self.assertTrue(False)

    ## def test_change_move(self):
    ##     self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
