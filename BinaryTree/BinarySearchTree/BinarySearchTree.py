# Replace ___ with your code

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root=root

    def insert(self, value, current_node=None):
        if not self.root:
            self.root=BinarySearchTreeNode(value)
            return 

        if current_node is None:
            current_node=self.root
        
        if value<current_node.data:

            if current_node.left is None:
                current_node.left=BinarySearchTreeNode(value)
                return
            
            else:
                self.insert(value,current_node.left)
        elif value>current_node.data:

            if current_node.right is None:
                current_node.right=BinarySearchTreeNode(value)
                return
            
            else:
                self.insert(value,current_node.right)

    #Time Complexity : O(h)
   

    def search(self, value, current_node=None):
        if not self.root:
            return None 

        if current_node is None:
            current_node=self.root

        if value==current_node.data:
            return True

        elif value<current_node.data:
            if current_node.left is None:
                return None
            return self.search(value,current_node.left)

        elif value>current_node.data:
            if current_node.right is None:
                return None
            return self.search(value,current_node.right)
    
    #Time Complexity : O(h)


    def delete(self, root, key):
        if root is None:
            return root

        if key<root.data:
            root.left=self.delete(root.left,key)

        elif key>root.data:
            root.right=self.delete(root.right,key)

        else:
            if not root.left:
                temp=root.right
                root=None
                return temp

            elif not root.right:
                temp=root.left
                root=None
                return temp
            
            temp=root.right
            while temp.left:
                temp=temp.left
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)

        return root
        
    #Time Complexity : O(h)


    def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes=[]

        if node:
            self.inorder_traversal(node.left,visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right,visited_nodes)

        return visited_nodes


bst=BinarySearchTree()

values=[8,6,10,5,7,9,11]

for value in values:
    bst.insert(value)

print(bst.inorder_traversal(bst.root))

dele = [5, 10]

for value in dele:
    bst.root = bst.delete(bst.root, value)

print(bst.inorder_traversal(bst.root))


