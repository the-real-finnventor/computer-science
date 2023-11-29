import unittest
from base import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self) -> None:
        self.dict = Dictionary()

    def moreSetUp(self) -> None:
        self.keys_and_values = [
            ("hi", "hello"), ("test", "testing"), ("idk", "i give up")]
        self.keys = []
        self.values = []
        for key, value in self.keys_and_values:
            self.dict.add(key, value)
            self.keys.append(key)
            self.values.append(value)

    def test_add(self):
        self.assertIsNone(self.dict.add("test", "yay"))

    def test_lookup(self):
        self.moreSetUp()
        self.assertEqual("testing", self.dict.lookup("test"))

    def test_keys(self):
        self.moreSetUp()
        self.assertEqual(set(self.keys), set(list(self.dict.keys())))

    def test_values(self):
        self.moreSetUp()
        self.assertEqual(set(self.values), set(list(self.dict.values())))

    def test_keys_and_values(self):
        self.moreSetUp()
        self.assertEqual(set(self.keys_and_values), set(
            list(self.dict.keys_and_values())))

    def test_for(self):
        self.moreSetUp()
        for key, value in self.dict:
            self.assertIn((key, value), self.keys_and_values)


if __name__ == "__main__":
    unittest.main()
