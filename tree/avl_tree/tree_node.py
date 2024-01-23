class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1

    def __str__(self) -> str:
        rv = ""
        if not self.l is None:
            rv += f"{self.l.__str__()} "
        rv += f"{self.value}"
        if not self.r is None:
            rv += f" {self.r.__str__()}"
        return rv

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if type(__value) == TreeNode and __value.value == self.value and __value.l == self.l and __value.r == self.r:
            return True
        return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        return hash(self.value)

    def find(self, key) -> 'TreeNode':
        if key == self.value:
            return self
        if key < self.value and self.l:
            return self.l.find(key)
        if key > self.value and self.r:
            return self.r.find(key)

    def findLargerThan(self, key) -> set:
        curr = set()
        if self.value > key:
            curr.add(self.value)
            if self.l:
                curr.update(self.l.findLargerThan(key))
        if self.r:
            curr.update(self.r.findLargerThan(key))
        return curr

    def findRange(self, start, end) -> set:
        curr = set()
        if self.value > start and self.value < end:
            curr.add(self.value)
        if self.value > start and self.l:
            curr.update(self.l.findRange(start, end))
        if self.value < end and self.r:
            curr.update(self.r.findRange(start, end))
        return curr
