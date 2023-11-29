from .tree_node import TreeNode


class AVLTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

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

    def getAll(self, root):
        if not root:
            return ""

        rv = "{0} ".format(root.value)
        rv += self.getAll(root.l)
        rv += self.getAll(root.r)
        return rv

    def __str__(self):
        root = self.root

        if not root:
            return ""

        rv = "{0} ".format(root.value)
        rv += self.getAll(root.l)
        rv += self.getAll(root.r)
        return rv

    def find(self, root, key):
        if not root:
            return False
        if key == root.value:
            return root
        if key < root.value:
            if root.l:
                return self.find(root.l, key)
            return False
        if key > root.value:
            if root.r:
                return self.find(root.r, key)
            return False
