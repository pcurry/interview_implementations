#!/usr/bin/env python2.7

import unittest

from webob import Request
from webob import Response
from webob import exc


from rest_api import RestfullToybot


class TestAPI(unittest.TestCase):

    def setUp(self):
        # Make API app
        super(TestAPI, self).setUp()
        self.app = RestfullToybot()

    def tearDown(self):
        # Clean up mess
        del self.app
        super(TestAPI, self).tearDown()

    def test_list_bots(self):
        sessionid = "abcd123"
        bots = app.list(sessionid)
        self.assertEqual([], bots)
        

    def test_create_bot(self):
        self.assertTrue(False)

    def test_recreate_bot(self):
        self.assertTrue(False)

    def test_place_bot(self):
        self.assertTrue(False)

    def test_replace_bot(self):
        self.assertTrue(False)

    def test_change_right(self):
        self.assertTrue(False)

    def test_change_left(self):
        self.assertTrue(False)

    def test_change_move(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
