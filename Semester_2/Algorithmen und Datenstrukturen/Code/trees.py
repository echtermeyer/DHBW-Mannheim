class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = Node(2, Node(1), Node(7, Node(4, Node(3)), Node(8)))
print(tree.value)
print(tree.left.value)
print(tree.right.value)
