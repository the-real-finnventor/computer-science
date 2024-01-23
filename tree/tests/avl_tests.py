import unittest
import sys
import os

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
import avl_tree


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = avl_tree.AVLTree()
        self.tree.root = self.tree.insert(0)
        self.tree.root = self.tree.insert(8)
        self.tree.root = self.tree.insert(4)
        self.tree.root = self.tree.insert(24)
        self.tree.root = self.tree.insert(-4)
        self.tree.root = self.tree.insert(12)

    def test_find(self):
        self.assertEqual(self.tree.find(-4), self.tree._root.l.l)
        self.assertEqual(self.tree.find(12), self.tree._root.r)

    def test_find_larger(self):
        self.assertEqual(self.tree.findLargerThan(4), set([8, 12, 24]))

    def test_find_range(self):
        self.assertEqual(self.tree.findRange(0, 24), set([4, 8, 12]))


if __name__ == "__main__":
    unittest.main()
