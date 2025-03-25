import unittest

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree(tree) -> BinaryTree:

    stack = [tree]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return tree

def tree_values(tree: BinaryTree) -> list:
    values = []
    def preorder_traversal(node: BinaryTree):
        if node:
            values.append(node.value)
            preorder_traversal(node.left)
            preorder_traversal(node.right)
    preorder_traversal(tree)
    return values

class TestInvertBinaryTreeFunc(unittest.TestCase):
    def test_invert_tree_func(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        self.assertEqual(tree_values(invert_binary_tree(root)), [1, 3, 7, 6, 2, 5, 4])

if __name__ == '__main__':
    unittest.main()
