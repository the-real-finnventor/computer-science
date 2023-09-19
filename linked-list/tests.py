import base
import unittest

ll = base.insertItems([5, 7, 8, 9, 2])
empty_ll = base.insertItems([])


class TestLL(unittest.TestCase):
    def test_len(self):
        self.assertEqual(ll.len(), 5)

    def test_empty_len(self):
        self.assertEqual(empty_ll.len(), 0)

    def test_find(self):
        actual = ll.find(2)
        self.assertIsNotNone(actual)
        self.assertEqual(actual.data, 2)

    def test_find_missing(self):
        self.assertIsNone(ll.find(11))


if __name__ == "__main__":
    unittest.main()
