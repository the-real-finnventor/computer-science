import unittest
from binary_search import binary_search


class BinarySearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list = [1, 24, 55, 82, 93, 174]

    def test_first(self):
        self.assertEqual(binary_search(self.test_list, 82), 3)

    def test_lower(self):
        self.assertEqual(binary_search(self.test_list, 24), 1)

    def test_upper(self):
        self.assertEqual(binary_search(self.test_list, 174), 5)

    def test_none(self):
        self.assertEqual(binary_search(self.test_list, 100), -1)

    def test_empty(self):
        self.assertEqual(binary_search([], 0), -1)


if __name__ == "__main__":
    unittest.main()
