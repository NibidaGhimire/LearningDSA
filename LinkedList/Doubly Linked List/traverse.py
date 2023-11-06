class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_linked_list(self):
        node1 = Node(80)
       
        self.head = node1
        self.tail = node1

        node2 = Node(9)
        node1.next = node2
        node2.prev = node1
        self.tail = node2

        node3 = Node(14)
        
        node2.next = node3
        node3.prev = node2
  
        self.tail = node3
    
    
    def traverse(self):
        # start at head
        current = self.head
        print("None <-> ", end = "")
        # loop until the node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")

linked_list = DoublyLinkedList()
linked_list.create_linked_list()
linked_list.traverse()


#Time Complexity : O(n)