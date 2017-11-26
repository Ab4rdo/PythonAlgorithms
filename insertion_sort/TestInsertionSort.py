import unittest

from insertion_sort.InsertionSort import sort


class TestInsertionSort(unittest.TestCase):

    def test_sort_1(self):
        arr = [1, 10, 1000, 100]
        aft_sort = sort(arr)
        self.assertEqual(aft_sort, [1, 10, 100, 1000])

    def test_sort_2(self):
        arr = [1, 10, 100, 1000]
        aft_sort = sort(arr)
        self.assertEqual(aft_sort, arr)

    def test_sort_with_empty_list(self):
        arr = []
        with self.assertRaises(ValueError):
            sort(arr)

if __name__ == '__main__':
    unittest.main()
