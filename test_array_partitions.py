


import unittest

import array_partitions


class TestEqualSum(unittest.TestCase):

    def setUp(self):
        self.equal_sum = array_partitions.equal_sum

    def test_empty_list(self):
        self.assertIsNone(self.equal_sum([]))

    def test_single_element_list(self):
        self.assertIsNone(self.equal_sum([3]))

    def test_balanced_pairs(self):
        case_1 = [1, 1]
        result_1 = self.equal_sum(case_1)
        self.assertEqual(result_1, ([1], [1]))
        case_2 = [1, 2, 1, 2]
        result_2 = self.equal_sum(case_2)
        self.assertEqual(result_2, ([1, 2], [1, 2]))

    def test_descending_list(self):
        case = [3, 2, 1]
        result = self.equal_sum(case)
        self.assertEqual(result, ([3], [2, 1]))

    def test_ascending_list(self):
        case = [1, 1, 2]
        result = self.equal_sum(case)
        self.assertEqual(result, ([1, 1], [2]))



class TestRecursiveEqualSum(TestEqualSum):

    def setUp(self):
        self.equal_sum = array_partitions.equal_sum_recursive


class TestTailRecursiveEqualSum(TestEqualSum):

    def setUp(self):
        self.equal_sum = array_partitions.equal_sum_tail_recursive


if __name__ == '__main__':
    unittest.main()
