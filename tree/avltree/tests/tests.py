import unittest

import src


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = src.AVLTree()
        self.tree.root = self.tree.insert(self.tree.root, 0)
        self.tree.root = self.tree.insert(self.tree.root, 8)
        self.tree.root = self.tree.insert(self.tree.root, 4)
        self.tree.root = self.tree.insert(self.tree.root, 24)
        self.tree.root = self.tree.insert(self.tree.root, -4)
        self.tree.root = self.tree.insert(self.tree.root, 12)

    def testFind(self):
        self.assertEqual(self.tree.find(
            self.tree.root, -4), self.tree.root.l.l)
        self.assertEqual(self.tree.find(
            self.tree.root, 12), self.tree.root.r)


if __name__ == "__main__":
    unittest.main()
