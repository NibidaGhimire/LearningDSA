
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self,root=None):
        self.root=root

    def node_at_level(self,node,k):
        if node is None:
            return []
        elif k==0:
            return [node.data]
        else:
            result=[]
            for child in node.children:
                result+=self.node_at_level(child,k-1)
            return result

root=TreeNode("root")

# create leaf nodes
lev1=TreeNode(1)
lev2=TreeNode(2)
lev3=TreeNode(3)

root.add_child(lev1)
lev1.add_child(lev2)
lev2.add_child(lev3)

tree=Tree(root)

for i in range(0,4):
    print(f"Nodes at Level {i}:",*[node for node in tree.node_at_level(root,i)])