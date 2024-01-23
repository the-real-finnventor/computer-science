from .stack.base import Stack
from icecream import ic
from typing import Mapping, Literal

operations = {
    "+": lambda a, b: b + a,
    "-": lambda a, b: b - a,
    "*": lambda a, b: b * a,
    "÷": lambda a, b: b / a,
    "/": lambda a, b: b / a
}


class TreeNode:
    def __init__(self, expression: str):
        if len(expression) == 1:
            self.value: str = expression
            self.l: TreeNode = None
            self.r: TreeNode = None
            return
        first_half = ""
        second_half = ""
        half = 1
        deep = 0
        for char in expression:
            if half == 1:
                if not ((deep == 0 and char == "(") or (deep == 1 and char == ")")):
                    first_half += char
            elif half == 2:
                if not ((deep == 0 and char == "(") or (deep == 1 and char == ")")):
                    second_half += char
            if char == "(":
                deep += 1
            elif char == ")":
                deep -= 1
            elif char in ["+", "-", "*", "÷", "/"] and deep == 0:
                self.value: str = char
                half = 2
                first_half: list = list(first_half)
                first_half[-1] = ""
                first_half: str = ''.join(first_half)
        self.l: TreeNode = TreeNode(first_half.strip())
        self.r: TreeNode = TreeNode(second_half.strip())

    def __str__(self) -> str:
        rv = ""
        if self.l:
            rv = "("
            rv += str(self.l) + " "
        rv += f"{self.value}"
        if self.r:
            rv += " " + str(self.r)
            rv += ")"
        return rv

    def __repr__(self) -> str:
        return self.__str__()

    def __compute(self, stack: Stack) -> Stack:
        if self.l:
            stack = self.l.__compute(stack)
        if self.r:
            stack = self.r.__compute(stack)
        if self.value.isnumeric():
            stack.push(int(self.value))
        elif self.value in ["+", "-", "*", "÷", "/"]:
            stack.push(operations[self.value](stack.pop(), stack.pop()))
        return stack

    def __int__(self) -> int:
        stack: Stack = Stack()
        return round(self.__compute(stack).pop())

    def compute(self) -> float:
        stack: Stack = Stack()
        return float(self.__compute(stack).pop())
