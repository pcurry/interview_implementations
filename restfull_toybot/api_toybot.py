#!/usr/bin/env python2.7

from collections import namedtuple


def go_north(x_pos, y_pos):
    return x_pos, y_pos + 1


def go_south(x_pos, y_pos):
    return x_pos, y_pos - 1


def go_east(x_pos, y_pos):
    return x_pos + 1, y_pos


def go_west(x_pos, y_pos):
    return x_pos - 1, y_pos


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

    def is_position_on_table(self, x, y):
        x_ok = self.x_min <= x and x <= self.x_max
        y_ok = self.y_min <= y and y <= self.y_max
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

    def __init__(self,
                 name,
                 x_pos=None,
                 y_pos=None,
                 angle=None,
                 on_table=False):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = COMPASS[angle] if angle else None
        self.on_table = on_table
        self.table = DEFAULT_TABLE

    def place(self, x_pos, y_pos, angle):
        if self.table.is_position_on_table(x_pos, y_pos):
            self.angle = COMPASS[angle]
            self.x_pos = x_pos
            self.y_pos = y_pos
            return self.report_orientation()
        else:
            raise BadStartingPositionError(
                "Starting position {}, {} not on the table".format(x_pos,
                                                                   y_pos)
            )

    def left(self):
        if self.on_table:
            self.angle = COMPASS[self.angle.left]
        else:
            raise NotOnTableException()

    def right(self):
        if self.on_table:
            self.angle = COMPASS[self.angle.right]
        else:
            raise NotOnTableException()

    def move(self):
        new_x, new_y = self.angle.move(self.x_pos, self.y_pos)
        if self.table.is_position_on_table(new_x, new_y):
            self.position = new_position
            return self.reprort_orientation()
        else:
            raise WouldFallOffTableError(
                "Cannot move to {}, {} -  that is off the table".format(
                    new_x, new_y
                )
            )

    def report_orientation(self):
        return {
            "angle": self.angle.name,
            "x_pos": self.x_pos
            "y_pos": self.y_pos
        }

    def persist(self):
        return {
            "name": self.name,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos,
            "angle": self.angle.name,
            "on_table": self.on_table
        }
