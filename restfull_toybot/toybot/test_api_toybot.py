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
        orientation = testbot.place(0, 1, "NORTH")
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

    def test_left_rotation(self):
        testbot = api_toybot.Robot("Testbot")
        testbot.place(1, 1, "NORTH")
        counterclockwise = ("WEST", "SOUTH", "EAST", "NORTH")
        for angle in counterclockwise:
            pre = testbot.report()
            self.assertNotEqual(angle, pre["angle"])
            post = testbot.left()
            self.assertEqual(angle, post["angle"])

    def test_right_rotation(self):
        testbot = api_toybot.Robot("Testbot")
        testbot.place(1, 1, "NORTH")
        clockwise = ("EAST", "SOUTH", "WEST", "NORTH")
        for angle in clockwise:
            pre = testbot.report()
            self.assertNotEqual(angle, pre["angle"])
            post = testbot.right()
            self.assertEqual(angle, post["angle"])

    def test_move_east(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(1, 1, "EAST")
        post = testbot.move()
        self.assertEqual(pre["angle"], post["angle"])
        self.assertEqual(pre["x_pos"] + 1, post["x_pos"])
        self.assertEqual(pre["y_pos"], post["y_pos"])

    def test_move_north(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(1, 1, "NORTH")
        post = testbot.move()
        self.assertEqual(pre["angle"], post["angle"])
        self.assertEqual(pre["x_pos"], post["x_pos"])
        self.assertEqual(pre["y_pos"] + 1, post["y_pos"])

    def test_move_south(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(1, 1, "SOUTH")
        post = testbot.move()
        self.assertEqual(pre["angle"], post["angle"])
        self.assertEqual(pre["x_pos"], post["x_pos"])
        self.assertEqual(pre["y_pos"] - 1, post["y_pos"])

    def test_move_west(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(1, 1, "WEST")
        post = testbot.move()
        self.assertEqual(pre["angle"], post["angle"])
        self.assertEqual(pre["x_pos"] - 1, post["x_pos"])
        self.assertEqual(pre["y_pos"], post["y_pos"])

    def test_east_edge(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(4, 1, "EAST")
        self.assertRaises(
            api_toybot.WouldFallOffTableError,
            testbot.move
        )

    def test_north_edge(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(0, 4, "NORTH")
        self.assertRaises(
            api_toybot.WouldFallOffTableError,
            testbot.move
        )

    def test_south_edge(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(2, 0, "SOUTH")
        self.assertRaises(
            api_toybot.WouldFallOffTableError,
            testbot.move
        )

    def test_west_edge(self):
        testbot = api_toybot.Robot("Testbot")
        pre = testbot.place(0, 1, "WEST")
        self.assertRaises(
            api_toybot.WouldFallOffTableError,
            testbot.move
        )


if __name__ == "__main__":
    unittest.main()
