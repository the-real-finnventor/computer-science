from .tree_node import TreeNode


class AVLTree(object):
    def __init__(self, root=None):
        self._root: TreeNode = root

    def __insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.l = self.__insert(root.l, key)
        else:
            root.r = self.__insert(root.r, key)

        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.value:
            return self.rRotate(root)

        if b < -1 and key > root.r.value:
            return self.lRotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def insert(self, key):
        self._root = self.__insert(self._root, key)

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def __str__(self):
        if not self._root:
            return ""
        return str(self._root)

    def __repr__(self) -> str:
        return self.__str__()

    def find(self, key) -> TreeNode:
        if not self._root:
            return
        return self._root.find(key)

    def findLargerThan(self, key) -> set:
        if not self._root:
            return set()
        return self._root.findLargerThan(key)

    def findRange(self, start, end) -> set:
        if not self._root:
            return set()
        return self._root.findRange(start, end)
