import unittest

from selection_sort.SelectionSort import *


class TestSelectionSort(unittest.TestCase):

    def test_index_of_min(self):
        arr = [12, 10, 100, 0, -10, 1]
        min_index = index_of_min(arr, 0)
        self.assertEqual(min_index, 4)

    def test_sort_1(self):
        arr = [1, 5, 2, 4, 10]
        aft_sort = sort(arr)
        self.assertEqual(aft_sort, [1, 2, 4, 5, 10])

    def test_sort_with_empty_list(self):
        arr = []
        with self.assertRaises(ValueError):
            sort(arr)


if __name__ == '__main__':
    unittest.main()