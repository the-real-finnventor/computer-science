class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

    def GetData(self) -> any:
        return self.data

    def GetLeft(self):
        return self.l

    def GetRight(self):
        return self.r

    def SetData(self, data):
        self.data = data
        return self

    def SetRight(self, right):
        self.r = right
        return self

    def SetLeft(self, left):
        self.r = left
        return self

    def __str__(self) -> str:
        return self.data.__str__()

    def __eq__(self, __value: object) -> bool:
        if type(__value) == type(self) and self.data == __value.data and self.children == __value.children:
            return True

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        return hash(self.data)

    def __repr__(self) -> str:
        return self.__str__()
