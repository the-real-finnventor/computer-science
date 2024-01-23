from .tree_node import TreeNode


class SyntaxTree:
    def __init__(self, expression: str):
        self.root: TreeNode = TreeNode(expression)

    def __str__(self) -> str:
        return str(self.root)

    def __repr__(self) -> str:
        return self.__str__()

    def __int__(self) -> int:
        return int(self.root)

    def compute(self) -> float:
        return self.root.compute()
