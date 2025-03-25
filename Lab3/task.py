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

def preorder_traversal(tree):
    if tree is not None:
        stack = [tree]

        while stack:
            node = stack.pop()
            print(node.value, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return tree

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.right.left = BinaryTree(5)

inverted_tree = invert_binary_tree(root)
preorder_traversal(inverted_tree)

print(" ")

root1 = BinaryTree(10)
root1.left = BinaryTree(20)
root1.right = BinaryTree(30)
root1.left.left = BinaryTree(45)
root1.right.left = BinaryTree(55)
root1.right.right = BinaryTree(60)

inverted_tree = invert_binary_tree(root1)
preorder_traversal(inverted_tree)
















