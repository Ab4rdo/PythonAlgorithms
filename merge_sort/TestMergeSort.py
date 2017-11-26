import unittest

from merge_sort.MergeSort import *


class TestMergeSort(unittest.TestCase):

    def test_merge_function_1(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        aft_merge = merge(arr1, arr2)
        self.assertEqual(aft_merge, [1, 2, 3, 4, 5, 6])

    def test_merge_function_2(self):
        arr1 = [3, 3, 5]
        arr2 = [2, 3, 6, 7]
        aft_merge = merge(arr1, arr2)
        self.assertEqual(aft_merge, [2, 3, 3, 3, 5, 6, 7])

    def test_sort_1(self):
        arr = [1, 0, 2, 4, 5, 3]
        aft_sort = sort(arr)
        self.assertEqual(aft_sort, [0, 1, 2, 3, 4, 5])

    def test_sort_2(self):
        arr = [100, -10, -100, 100, 100]
        aft_sort = sort(arr)
        self.assertEqual(aft_sort, [-100, -10, 100, 100, 100])


if __name__ == '__main__':
    unittest.main()