
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
    
    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root=root
    
    def postorder_traversal(self, node, traversal=[]):
        if node is None:
            return traversal

        for child in node.children:
            self.postorder_traversal(child,traversal)

        traversal.append(node.data)
        return traversal

root=TreeNode("A")
c11=TreeNode("B")
c21=TreeNode("B1")
c22=TreeNode("B2")
c31=TreeNode("B1_1")

root.add_child(c11)
c11.add_child(c21)
c11.add_child(c22)
c21.add_child(c31)

tree=Tree(root)
print(tree.postorder_traversal(root))