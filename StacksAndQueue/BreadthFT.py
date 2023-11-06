from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    
    def add_child(self,child):
        self.children.append(child)
class Tree:
    def __init__(self,root=None):
        self.root=root
    
    def breadth_first_traversal(self,root=None):
        if not self.root:
            return []

        traversal=[]
        queue=deque()
        queue.append(self.root)
        while queue:
            cur_node=queue.popleft()
            traversal.append(cur_node.data)
            for child in cur_node.children:
                queue.append(child)
        return traversal

A=TreeNode("A")
B=TreeNode("B")
C=TreeNode("C")
D=TreeNode("D")
E=TreeNode("E")
F=TreeNode("F")
G=TreeNode("G")

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
E.add_child(G)

tree=Tree(A)
print(tree.breadth_first_traversal(tree.root))