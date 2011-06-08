
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
        self.assertNotEquals(output[0], output[1])
        order_same = output == source
        order_reversed = output == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")


class TestRandomizeListInPlace(unittest.TestCase):

    def test_two_element_list(self):
        first = "first"
        second = "second"
        source = [first, second]
        check = list(source)
        randomlist.randomize_list_in_place(source)
        self.assertEquals(2, len(source), "Number of elements changed.")
        self.assertEquals(set(check), set(source),
                          "Elements changed.")
        self.assertNotEquals(source[0], source[1])
        order_same = check == source
        order_reversed = source == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")
        


# FIXME: There is a cleverer way to test all the randomization methods
# FIXME: against the same set of tests. I don't remember how exactly
# FIXME: at the moment, and I want these tests up now, but I will fix 
# FIXME: this later.

class TestRandomizeListAppend(unittest.TestCase):

    def test_two_element_list(self):
        first = "first"
        second = "second"
        source = [first, second]
        output = randomlist.randomize_list_append(source)
        self.assertEquals(2, len(output), "Number of elements changed.")
        self.assertEquals(set(source), set(output),
                          "Elements changed.")
        self.assertNotEquals(output[0], output[1])
        order_same = output == source
        order_reversed = output == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")


class TestRandomizeListComprehension(unittest.TestCase):

    def test_two_element_list(self):
        first = "first"
        second = "second"
        source = [first, second]
        output = randomlist.randomize_list_comprehension(source)
        self.assertEquals(2, len(output), "Number of elements changed.")
        self.assertEquals(set(source), set(output),
                          "Elements changed.")
        self.assertNotEquals(output[0], output[1])
        order_same = output == source
        order_reversed = output == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")


class TestRandomizeListInsert(unittest.TestCase):

    def test_two_element_list(self):
        first = "first"
        second = "second"
        source = [first, second]
        output = randomlist.randomize_list_insert(source)
        self.assertEquals(2, len(output), "Number of elements changed.")
        self.assertEquals(set(source), set(output),
                          "Elements changed.")
        self.assertNotEquals(output[0], output[1])
        order_same = output == source
        order_reversed = output == [second, first]
        self.assert_(order_same or order_reversed,
                     "The order is weird.")



class TestRandomGenerator(unittest.TestCase):
    pass 



if __name__ == "__main__":
    unittest.main()
