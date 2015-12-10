#!/usr/bin/env python2.7

import unittest

import api_toybot


class TestToybot(unittest.TestCase):

    def test_unplaced_bot(self):
        testbot = api_toybot.Robot("Testbot")
        self.assertRaises(api_toybot.NotOnTableException, testbot.left)
        self.assertRaises(api_toybot.NotOnTableException, testbot.right)
        self.assertRaises(api_toybot.NotOnTableException, testbot.move)
        self.assertRaises(api_toybot.NotOnTableException, testbot.report)

    def test_bot_placement(self):
        testbot = api_toybot.Robot("Testbot")
        self.assertRaises(api_toybot.NotOnTableException, testbot.report)
        testbot.place(0, 1, "NORTH")
        orientation = testbot.report()
        self.assertEqual(0, orientation["x_pos"])
        self.assertEqual(1, orientation["y_pos"])
        self.assertEqual("NORTH", orientation["angle"])

    def test_invalid_bot_placement(self):
        testbot = api_toybot.Robot("Testbot")
        self.assertRaises(
            api_toybot.BadStartingPositionError,
            testbot.place,
            -1,
            0,
            "EAST"
        )
        self.assertRaises(
            api_toybot.BadStartingPositionError,
            testbot.place,
            1,
            7,
            "EAST"
        )
        self.assertRaises(
            api_toybot.InvalidAngleError,
            testbot.place,
            1,
            2,
            "NOT_AN_ANGLE"
        )


if __name__ == "__main__":
    unittest.main()
