


import unittest

from array_partitions import equal_sum


class TestEqualSum(unittest.TestCase):


    def test_empty_list(self):
        self.assertIsNone(equal_sum([]))

    def test_single_element_list(self):
        self.assertIsNone(equal_sum([3]))

    def test_balanced_pairs(self):
        case_1 = [1, 1]
        result_1 = equal_sum(case_1)
        self.assertEqual(result_1, ([1], [1]))
        case_2 = [1, 2, 1, 2]
        result_2 = equal_sum(case_2)
        self.assertEqual(result_2, ([1, 2], [1, 2]))

    def test_descending_list(self):
        case = [3, 2, 1]
        result = equal_sum(case)
        self.assertEqual(result, ([3], [2, 1]))

    def test_ascending_list(self):
        case = [1, 1, 2]
        result = equal_sum(case)
        self.assertEqual(result, ([1, 1], [2]))


if __name__ == '__main__':
    unittest.main()
