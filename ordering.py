
"""
Sample Data (min, max, return_value):
  - (1, 10, 1)
  - (11, 50, 5)
  - (51, 100, 10)
  - (101, 500, 50)
  - (501, 1000, 100)
  - (1001, 5000, 500)
  - (5001, 10000, 1000)
"""

import math
import random


def round_order(x):
    if x < 1:
        raise ValueError(x)

    log_x = math.log(x, 10)
    if log_x <= 1:
        return 1

    order_floor = math.floor(log_x)
    result_multiple = 10 ** (order_floor - 1)
    test_multiple = 10 ** order_floor
    split_on = 5 * test_multiple
    
    if log_x == order_floor:
        return result_multiple

    elif log_x > order_floor and x <= split_on:
        return 5 * result_multiple

    elif x > split_on and log_x < (order_floor + 1):
        return test_multiple

    else:
        raise ValueError(x)


def test_round_order(minimum, maximum, return_value):
    for y in range(minimum, maximum + 1):
        assert(round_order(y) == return_value)


if __name__ == '__main__':

    test_data = [
                 (1, 10, 1),
                 (11, 50, 5),
                 (51, 100, 10),
                 (101, 500, 50),
                 (501, 1000, 100),
                 (1001, 5000, 500),
                 (5001, 10000, 1000)
    ]

    for test_values in test_data:
        test_round_order(*test_values)
