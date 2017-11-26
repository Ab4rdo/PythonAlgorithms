import unittest

from binary_search.BinarySearch import search


class TestBinarySearch(unittest.TestCase):

    def test_search_1(self):
        arr = [10, 100, 1000, 10000]
        target_index = search(arr, 1000)
        self.assertEqual(target_index, 2)

    def test_search_2(self):
        arr = [10, 100, 1000, 10000]
        target = -100
        with self.assertRaises(ValueError):
            search(arr, target)

    def test_search_empty_list(self):
        arr = []
        with self.assertRaises(ValueError):
            search(arr, 0)

    def test_search_value_not_included(self):
        arr = [1, 2, 3, 4, 5, 6]
        target = 100
        with self.assertRaises(ValueError):
            search(arr, target)


if __name__ == '__main__':
    unittest.main()