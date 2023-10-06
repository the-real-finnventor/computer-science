import unittest
import base


class TestLL(unittest.TestCase):
    def setUp(self):
        self.ll = base.LinkedList.insertItems([5, 7, 8, 9, 2])

    def test_len(self):
        self.assertEqual(self.ll.len(), 5)

    def test_empty_len(self):
        self.empty_ll = base.LinkedList.insertItems([])
        self.assertEqual(self.empty_ll.len(), 0)

    def test_find(self):
        actual = self.ll.find(2)
        self.assertIsNotNone(actual)
        self.assertEqual(actual.data, 2)

    def test_find_missing(self):
        self.assertIsNone(self.ll.find(11))

    def test_insert_at(self):
        self.ll.insert_at(65, 3)
        self.assertIsNotNone(self.ll.find(65))
        self.assertEqual(self.ll.getLL(), [5, 7, 8, 65, 9, 2])

    def test_insert_at_past_end(self):
        with self.assertRaises(base.LinkedListError):
            self.ll.insert_at(5, 1000)

    def test_insert_front_1(self):
        self.ll.insert_front(73)
        self.assertIsNotNone(self.ll.find(73))
        self.assertEqual(self.ll.getLL(), [73, 5, 7, 8, 9, 2])

    def test_insert_front_2(self):
        self.ll.insert_front(0)
        self.assertIsNotNone(self.ll.find(0))
        self.assertEqual(self.ll.getLL(), [0, 5, 7, 8, 9, 2])

    def test_insert_end_1(self):
        self.ll.insert_end(86)
        self.assertIsNotNone(self.ll.find(86))
        self.assertEqual(self.ll.getLL(), [5, 7, 8, 9, 2, 86])
        self.assertIsNone(self.ll.find(86).nextNode)

    def test_insert_end_2(self):
        self.ll.insert_end(24)
        self.assertIsNotNone(self.ll.find(24))
        self.assertEqual(self.ll.getLL(), [5, 7, 8, 9, 2, 24])
        self.assertIsNone(self.ll.find(24).nextNode)

    def test_has_cycle_1(self):
        self.ll.find(2).nextNode = self.ll.find(5)
        self.assertTrue(self.ll.has_cycle())

    def test_has_cycle_2(self):
        self.ll.find(9).nextNode = self.ll.find(9)
        self.assertTrue(self.ll.has_cycle())

    def test_has_cycle_3(self):
        self.ll.find(9).nextNode = self.ll.find(7)
        self.assertTrue(self.ll.has_cycle())

    def test_has_cycle_4(self):
        self.assertFalse(self.ll.has_cycle())


if __name__ == "__main__":
    unittest.main()
