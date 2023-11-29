from .morse_code_tree_error import MorseCodeTreeError
from .node import Node


class MorseCodeTree:
    def __init__(self):
        self.root = Node('root')

    def GetRoot(self) -> Node:
        return self.root

    def SetRoot(self, root: Node):
        self.root = root
        return self

    def DecodeLetter(self, data: str) -> str:
        if data == '/':
            return ' '
        curr = self.GetRoot()
        for direction in data:
            if not curr:
                return
            if direction == '.':
                curr = curr.GetLeft()
            elif direction == '-':
                curr = curr.GetRight()
            else:
                raise MorseCodeTreeError(
                    'Morse Code letters contain only "."s or "-"s')
        return curr.GetData()

    def DecodeWord(self, data: str) -> str:
        word = ""
        for letter in data.split(' '):
            word += self.DecodeLetter(letter)
        return word.strip()

    def Decode(self, data: str) -> str:
        rv = ""
        for word in data.split('   '):
            rv += self.DecodeWord(word)
            rv += ' '
        return rv.strip()
