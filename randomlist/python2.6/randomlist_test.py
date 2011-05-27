
import unittest

# Module under test
import randomlist

class TestRandomList(unittest.TestCase):

    def test_single_element(self):
        source = ["foo"]
        output = randomlist.random_list(source)
        self.assertEquals(source, output,
                          "Didn't return the same element as a list")

    def test_two_element_list(self):
        first = "first"
        second = "second"
        source = [first, second]
        output = randomlist.random_list(source)
        self.assertEquals(2, len(output), "Number of elements changed.")
        self.assertEquals(set(source), set(output),
                          "Elements changed.")
        order_same = output == source
        order_reversed = output == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")



class TestRandomGenerator(unittest.TestCase):
    pass 



if __name__ == "__main__":
    unittest.main()
