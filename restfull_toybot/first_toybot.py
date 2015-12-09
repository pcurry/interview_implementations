#!/usr/bin/env python2.7

from collections import namedtuple


Position = namedtuple("Position", ["x_pos", "y_pos"])


def go_north(position):
    return Position(position.x_pos, position.y_pos + 1)


def go_south(position):
    return Position(position.x_pos, position.y_pos - 1)


def go_east(position):
    return Position(position.x_pos + 1, position.y_pos)


def go_west(position):
    return Position(position.x_pos - 1, position.y_pos)


Direction = namedtuple("Direction", ["name", "left", "right", "move"])


COMPASS = {
    "NORTH": Direction("NORTH", "WEST", "EAST", go_north),
    "EAST": Direction("EAST", "NORTH", "SOUTH", go_east),
    "SOUTH": Direction("SOUTH", "EAST", "WEST", go_south),
    "WEST": Direction("WEST", "SOUTH", "NORTH", go_west),
}


class Table(object):

    def is_position_on_table(self, position):
        return False


class RectangularTable(Table):

    def __init__(self, x_min, x_max, y_min, y_max):
        super(RectangularTable, self).__init__()
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def is_position_on_table(self, position):
        x_ok = self.x_min <= position.x_pos and postition.x_pos <= self.x_max
        y_ok = self.y_min <= position.y_pos and postition.y_pos <= self.y_max
        return x_ok and y_ok


class SquareTable(RectangularTable):

    def __init__(self, x_min, y_min, side_length):
        super(SquareTable, self).__init__(
            x_min,
            x_min + side_length - 1,
            y_min,
            x_min + side_length - 1,
        )


DEFAULT_TABLE = SquareTable(0, 0, 5)


class WouldFallOffTableError(ValueError):
    pass


class BadStartingPositionError(WouldFallOffTableError):
    pass


class NotOnTableException(Exception):
    pass


class Robot(object):

    def __init__(self, name):
        self.name = name
        self.position = None
        self.angle = None
        self.table = None

    def place(self, x_pos, y_pos, angle, table=None):
        new_table = table if table else DEFAULT_TABLE
        new_position = Position(x_pos, y_pos)
        if new_table.is_position_on_table(new_position):
            self.table = new_table
            self.angle = COMPASS[angle]
            self.position = new_position
            return self.report_orientation()
        else:
            raise BadStartingPositionError(
                "Starting position {} not on the table".format(new_position)
            )

    def left(self):
        if self.table:
            self.angle = COMPASS[self.angle.left]
        else:
            raise NotOnTableException()

    def right(self):
        if self.table:
            self.angle = COMPASS[self.angle.right]
        else:
            raise NotOnTableException()

    def move(self):
        new_position = self.angle.move(self.position)
        if self.table.is_position_on_table(new_position):
            self.position = new_position
            return self.reprort_orientation()
        else:
            raise WouldFallOffTableError(
                "Cannot move to {}, that is off the edge of the table".format(
                    new_position
                )
            )

    def report_orientation(self):
        return {
            "angle": self.angle.name,
            "x_pos": self.position.x_pos,
            "y_pos": self.position.y_pos
        }


# Should have the API
#
