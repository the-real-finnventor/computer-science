import unittest
from merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(merge_sort([0, -2, 4, 6, 3]), [-2, 0, 3, 4, 6])

    def test_sorted(self):
        self.assertEqual(merge_sort([-2, 0, 3, 4, 6]), [-2, 0, 3, 4, 6])

    def test_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_one_item(self):
        self.assertEqual(merge_sort([0]), [0])


if __name__ == "__main__":
    unittest.main()
