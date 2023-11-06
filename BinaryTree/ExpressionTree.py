class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def inorder_and_evaluate(self, node):
        if node is None:
            return "", 0

        if not node.left and not node.right:
            return str(node.data), int(node.data)

        left_expr, left_val = self.inorder_and_evaluate(node.left)
        right_expr, right_val = self.inorder_and_evaluate(node.right)

        combined_expr = f"({left_expr} {node.data} {right_expr})"
        
        if node.data == '+':
            return combined_expr, left_val + right_val
        elif node.data == '-':
            return combined_expr, left_val - right_val
        elif node.data == '*':
            return combined_expr, left_val * right_val
        elif node.data == '/':
            return combined_expr, left_val / right_val

root_node = BinaryTreeNode("-")
node1 = BinaryTreeNode("/")
node2 = BinaryTreeNode("+")
node3 = BinaryTreeNode("*")
node4 = BinaryTreeNode("+")
node5 = BinaryTreeNode("*")
node6 = BinaryTreeNode("6")
node7 = BinaryTreeNode("+")
node8 = BinaryTreeNode("3")
node9 = BinaryTreeNode("-")
node10 = BinaryTreeNode("2")
node11 = BinaryTreeNode("3")
node12 = BinaryTreeNode("-")
node13 = BinaryTreeNode("3")
node14 = BinaryTreeNode("1")
node15 = BinaryTreeNode("9")
node16 = BinaryTreeNode("5")
node17 = BinaryTreeNode("7")
node18 = BinaryTreeNode("4")

root_node.add_left_child(node1)
root_node.add_right_child(node2)

node1.add_left_child(node3)
node1.add_right_child(node4)

node2.add_left_child(node5)
node2.add_right_child(node6)

node3.add_left_child(node7)
node3.add_right_child(node8)

node4.add_left_child(node9)
node4.add_right_child(node10)

node5.add_left_child(node11)
node5.add_right_child(node12)

node7.add_left_child(node13)
node7.add_right_child(node14)

node9.add_left_child(node15)
node9.add_right_child(node16)

node12.add_left_child(node17)
node12.add_right_child(node18)

tree = BinaryTree(root_node)
expression, result = tree.inorder_and_evaluate(tree.root)
print(expression)
print(result)