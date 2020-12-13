import unittest
from random import randint, shuffle
from TestLinkedList import LinkedList


class A18Tests(unittest.TestCase):

    # Tests insert_first() method. The whole process should
    # not generate any errors
    def test_insert_first(self):
        a_list = LinkedList()
        for i in range(20):
            length = randint(i, i * 10)
            for j in range(length):
                a_list.insert_first(randint(-100, 100))

    # Tests insert_last() method. The whole process should
    # not generate any errors
    def test_insert_last(self):
        a_list = LinkedList()
        for i in range(20):
            length = randint(i, i * 10)
            for j in range(length):
                a_list.insert_last(randint(-100, 100))

    # Tests the get_num_links method.
    # Randomly inserts elements into the list, test the final number of links
    def test_num_links(self):
        test_list = LinkedList()
        size = randint(20, 60)

        for _ in range(size):
            test_list.insert_first(randint(-100, 100))
            test_list.insert_last(randint(-100, 100))

        self.assertEqual(size * 2, test_list.get_num_links())

    # Tests the __str__ method with list of fixed length.
    def test_str_fixed(self):
        test_list = LinkedList()
        # Insert 22 elements to the list
        for i in range(22):
            test_list.insert_last(i)

        expected = ('0  1  2  3  4  5  6  7  8  9\n'
                    '10  11  12  13  14  15  16  17  18  19\n'
                    '20  21')
        actual = str(test_list)
        self.assertTrue(self.check_str_equals(expected, actual))

    # Tests the __str__ method with randomly generated list
    def test_str_random(self):
        random_list = [randint(-100, 100) for _ in range(randint(20, 60))]
        test_list = LinkedList()

        for val in random_list[::-1]:
            test_list.insert_first(val)

        expected = self.create_str_of_list(random_list)
        actual = str(test_list)

        self.assertTrue(self.check_str_equals(expected, actual))

    # Tests the insert_in_order method.
    # Creates an ordered list and add some numbers to the list
    # using insert_in_order.
    def test_insert_in_order(self):
        another_list = []
        test_list = LinkedList()

        # Create an ordered list
        for i in range(-20, 40, 2):
            test_list.insert_last(i)
            another_list.append(i)

        # Insert the element that smaller than any values in the list
        test_list.insert_in_order(-40)
        another_list.append(-40)
        # Insert the element that suppose appear in the middle of the list
        test_list.insert_in_order(3)
        another_list.append(3)
        # Insert the element that already appear in the list
        test_list.insert_in_order(22)
        another_list.append(22)
        # Insert the element that bigger than any values in the list
        test_list.insert_in_order(75)
        another_list.append(75)

        another_list.sort()
        a_list = self.create_list_of_str(str(test_list))

        self.assertEqual(another_list, a_list)

    # Tests the find_unordered method of LinkedList.
    # Creates a LinkedList with the 100 random number from -50 to 50 and
    # searches elements that supposed to be in the LinkedList
    def test_find_unordered_1(self):
        # Create an list contains the integers from -50 to 50
        # and randomized the values in the list
        another_list = [*range(-50, 51)]
        shuffle(another_list)

        # Add the values from the list to a LinkedList
        test_list = LinkedList()
        for value in another_list:
            test_list.insert_last(value)

        # Search the first element in a_list, the value should also in LinkedList
        value = another_list[0]
        link = test_list.find_unordered(value)
        self.assertTrue(link is not None and self.get_value_from_link(link) == value)

        # Search 10 elements that suppose to be in the list
        for _ in range(10):
            value = another_list[randint(0, 100)]
            link = test_list.find_unordered(value)
            # Returned link should not be None and contains the value we're searching for
            ans = link is not None and self.get_value_from_link(link) == value
            self.assertTrue(ans)

        # Search for the last element in a_list, the value should also in LinkedList
        value = another_list[len(another_list) - 1]
        link = test_list.find_unordered(value)
        self.assertTrue(link is not None and self.get_value_from_link(link) == value)

    # Tests the find_unordered method from the LinkedList
    # All the values we're looking for are not in the list, so the
    # method should return None each time.
    def test_find_unordered_2(self):
        # Create an list contains the integers from -50 to 50
        # and randomized the values in the list
        another_list = [*range(-50, 51)]
        shuffle(another_list)

        # Add the values from the list to a LinkedList
        test_list = LinkedList()
        for value in another_list:
            test_list.insert_last(value)

        results = []

        # Search 5 elements that suppose to NOT be in the list
        for _ in range(5):
            value = randint(-200, -51)
            link = test_list.find_unordered(value)
            # Returned link should be None
            ans = link is None
            results.append(ans)
        # Search another 5 elements that suppose to NOT be in the list
        for _ in range(5):
            value = randint(52, 200)
            link = test_list.find_unordered(value)
            # Returned link should be None
            ans = link is None
            results.append(ans)

        # all answers in the results list should be True
        self.assertTrue(all(results))

    # Tests the find_ordered() method from LinkedList.
    # All the values we're looking for should be in the LinkedList
    # which means the find_ordered() method will not return None
    def test_find_ordered_1(self):
        # Creates a list contains 100 random numbers then sort the list
        a_list = [randint(-100, 100) for _ in range(100)]
        a_list.sort()

        # Add the value in the sorted order to a LinkedList
        test_list = LinkedList()
        for val in a_list[::-1]:
            test_list.insert_first(val)

        # Search the first element in a_list, the value should also in LinkedList
        value = a_list[0]
        link = test_list.find_ordered(value)
        self.assertTrue(link is not None and self.get_value_from_link(link) == value)

        # Search 20 elements that supposed to in the LinkedList
        for _ in range(20):
            value = a_list[randint(0, len(a_list) - 1)]
            link = test_list.find_ordered(value)
            # Returned link should not be None and contains the same data
            ans = link is not None and self.get_value_from_link(link) == value
            self.assertTrue(ans)

        # Search for the last element in a_list, the value should also in LinkedList
        value = a_list[len(a_list) - 1]
        link = test_list.find_ordered(value)
        self.assertTrue(link is not None and self.get_value_from_link(link) == value)

    # Tests the find_ordered() method from LinkedList.
    # This time we are looking for the values not in the LinkedList.
    # So, the returned links should all be None
    def test_find_ordered_2(self):
        # Creates a list contains 100 random numbers then sort the list
        a_list = [randint(-100, 100) for _ in range(100)]
        a_list.sort()

        # Add the value in the sorted order to a LinkedList
        test_list = LinkedList()
        for val in a_list[::-1]:
            test_list.insert_first(val)

        # Search 20 elements that supposed to not in the LinkedList
        b_list = ([randint(-300, -101) for _ in range(10)]
                  + [randint(101, 300) for _ in range(10)])
        for value in b_list:
            link = test_list.find_ordered(value)
            # Returned link should not be None and contains the same data
            ans = link is None
            self.assertTrue(ans)

    # Tests the delete_link() method from LinkedList
    # The test will try to delete links already in the LinkedList
    def test_delete_link(self):
        # Create a LinkedList contains 200 random numbers from -100 to 100
        a_list = [*range(-100, 100)]
        shuffle(a_list)

        test_list = LinkedList()
        for value in a_list:
            test_list.insert_first(value)

        # Randomly delete 20 elements that in the LinkedList
        for _ in range(20):
            value = a_list.pop(randint(0, len(a_list) - 1))
            deleted = test_list.delete_link(value)
            # The link returned should not be None and has the same numeric data
            self.assertTrue(deleted is not None
                            and self.get_value_from_link(deleted) == value)
            # The value should not in the LinkedList anymore
            self.assertEqual(None, test_list.find_unordered(value))

        # Randomly delete 20 elements that are not in the LinkedList
        for _ in range(10):
            value = randint(-300, -101)
            deleted = test_list.delete_link(value)
            self.assertEqual(None, deleted)
            value = randint(101, 300)
            deleted = test_list.delete_link(value)
            self.assertEqual(None, deleted)

    # Tests the is_equal() method from LinkedList
    # Test cases contains:
    # two empty list, two list with same data, two list with different length
    # a non-empty list and an empty list
    def test_is_equal(self):
        a_list = LinkedList()
        b_list = LinkedList()
        # Two empty lists should equal to each other
        self.assertTrue(a_list.is_equal(b_list))

        for _ in range(200):
            value = randint(-100, 100)
            a_list.insert_last(value)
            b_list.insert_last(value)
        # Two lists with same value should equal to each other
        self.assertTrue(b_list.is_equal(a_list))

        for i in range(10):
            b_list.insert_last(i)
        # Two lists with different length should not equal
        self.assertFalse(a_list.is_equal(b_list))

        b_list = LinkedList()
        # a non-empty list and an empty list should not equal
        self.assertFalse(b_list.is_equal(a_list))

    # Tests is_empty() method from LinkedList.
    def test_is_empty(self):
        a_list = LinkedList()
        # should return true for an empty list
        self.assertTrue(a_list.is_empty(), msg='List suppose to be empty')

        # list should not be empty after insertion
        values = []
        for _ in range(200):
            value = randint(-50, 50)
            values.append(value)
            a_list.insert_last(value)
        self.assertFalse(a_list.is_empty(), msg='List suppose to be non-empty')

        # delete all the links from the LinkedList
        for value in values:
            a_list.delete_link(value)
        self.assertTrue(a_list.is_empty(), msg='List suppose to be empty after deletion')

    # Tests copy_list() method from LinkedList.
    def test_copy_list(self):
        a_list = LinkedList()

        for _ in range(200):
            a_list.insert_first(randint(-50, 50))
        b_list = a_list.copy_list()
        # b_list should not be empty, and two lists should be the same
        self.assertEqual(str(a_list), str(b_list), msg='__str__() should '
                                                       'return the same result')

    # Tests reverse_list() method from LinkedList.
    def test_reverse_list(self):
        a_list = LinkedList()
        a_reversed = LinkedList()
        for _ in range(200):
            value = randint(-50, 50)
            a_list.insert_last(value)
            a_reversed.insert_first(value)

        b_list = a_list.reverse_list()
        self.assertEqual(str(a_reversed), str(b_list))

    # Tests is_sorted() method from LinkedList.
    def test_is_sorted(self):
        a_list = LinkedList()
        a_list.insert_last(10)
        # A list with single element is seen as sorted
        self.assertTrue(a_list.is_sorted(), msg='List with one element is sorted')

        # Create a sorted list
        a_list = LinkedList()
        for i in range(-100, 101):
            a_list.insert_last(i)
        self.assertTrue(a_list.is_sorted())

        # Add some duplicate to the list, the list is still sorted
        for i in range(-25, 25):
            a_list.insert_in_order(i)
        self.assertTrue(a_list.is_sorted())

        # Add some elements to the front and tail of the list
        a_list.insert_first(-101)
        a_list.insert_first(-105)
        a_list.insert_last(100)
        a_list.insert_last(105)
        self.assertTrue(a_list.is_sorted())

        # Add eleemnt that make the list not sorted
        a_list.insert_last(99)
        self.assertFalse(a_list.is_sorted())

    # Tests sort_list() method from LinkedList.
    def test_sort_list(self):
        a_list = LinkedList()

        # Add elements in ascending order to the list
        for value in range(100, -100, -1):
            a_list.insert_first(value)
        b_list = a_list.sort_list()
        # The two lists should all be sorted and equal
        self.assertTrue(b_list.is_sorted())

        # Add random element to the list
        values = []
        a_list = LinkedList()
        for _ in range(100):
            value = randint(-50, 50)
            a_list.insert_first(value)
            values.append(value)
        b_list = a_list.sort_list()
        self.assertTrue(b_list.is_sorted())

    # Tests merge_list() method from LinkedList.
    def test_merge_list(self):
        a_list = LinkedList()
        b_list = LinkedList()

        # Merge two lists with same length
        for i in range(-50, 50, 2):
            a_list.insert_last(i)
            b_list.insert_last(i + 1)
        c_list = b_list.merge_list(a_list)
        # Merged list should also be sorted
        self.assertTrue(c_list.is_sorted())
        self.assertEqual(100, c_list.get_num_links())

        # Merge two lists with different length
        a_list = LinkedList()
        b_list = LinkedList()
        for value in range(200, 0, -1):
            a_list.insert_first(value)
            b_list.insert_first(value)
            b_list.insert_first(value)
        c_list = a_list.merge_list(b_list)
        self.assertEqual(600, c_list.get_num_links())

    # Tests remove_duplicate() method from LinkedList
    def test_remove_duplicate(self):
        # Remove duplicate from an empty list
        a_list = LinkedList()

        # Remove duplicates from a list where each item only appear once
        for i in range(-50, 50):
            a_list.insert_first(i)

        for i in range(50, -51, -1):
            a_list.insert_first(i)

        b_list = a_list.remove_duplicates()
        # Remove the data from b_list, after removal the data should not exit in b_list
        for data in range(-10, 10):
            b_list.delete_link(data)
            link = b_list.find_unordered(data)
            self.assertTrue(link is None)

    # Tests remove_duplicate() method for random numbers
    def test_remove_duplicate2(self):
        for i in range(20):
            # a_list will contain duplicates, b_list will not contain duplicate
            a_list = LinkedList()
            values = set()
            for _ in range(i * 10):
                value = randint(-10, 10)
                a_list.insert_last(value)
                values.add(value)
            b_list = a_list.remove_duplicates()
            values = list(values)
            for i in range(len(values) // 5):
                # Remove the data from b_list, after removal the data should not exit in b_list
                b_list.delete_link(values[i])
                link = b_list.find_unordered(values[i])
                self.assertTrue(link is None)

    @staticmethod
    def check_str_equals(str1, str2):
        """Checks if the two strings are equal to each other
            The only difference allowed is the spaces at the end of each line.

            For example:
            str1 = '0  1  2  3  4  5  6  7  8  9'
            str2 = '0  1  2  3  4  5  6  7  8  9  '

            Those two are equal to each other.

        Returns:
            True if two string are equals.
            False otherwise"""
        for line1, line2 in zip(str1.split('\n'), str2.split('\n')):
            if not line1.rstrip() == line2.rstrip():
                return False
        return True

    @staticmethod
    def create_str_of_list(l):
        """Creates a string representation of the list.

            The string should have 10 item per line and two spaces between them

        Args:
            l: a list of integer used to create the string

        Returns:
            The string generated from the list"""
        output = []
        size = len(l)
        for i in range(size // 10 + 1):
            start_idx = i * 10
            end_idx = min(start_idx + 10, size)
            values = [str(l[j]) for j in range(start_idx, end_idx)]
            output.append('  '.join(values))
        return '\n'.join(output)

    @staticmethod
    def get_value_from_link(link):
        """Returns the numeric value contains in the given Link object

        Args:
            link: A Link object that has a numeric value and a reference to next Link

        Returns:
            An integer in that Link object. None if not found"""
        if isinstance(link, int):
            return link
        attributes = link.__dict__
        for attr in attributes:
            value = attributes[attr]
            if isinstance(value, int):
                return value
        return None

    @staticmethod
    def create_list_of_str(strng):
        """Creates a list contains all the numbers from a string"""
        lines = strng.split()
        return [int(data) for data in lines]


if __name__ == '__main__':
    unittest.main()
