from tree.syntax_tree import SyntaxTree

tree = SyntaxTree("(2 / (8 * (4 ÷ 2))) + 9")
print(tree.compute())
