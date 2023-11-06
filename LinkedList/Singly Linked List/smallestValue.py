# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # method to append nodes
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node
        
    # method to return the smallest number 
    def find_smallest(self):
        current=self.head

        smallest=current.data

        if self.head.next==None:
            return current.data
        
        while current.next:
            if current.data<smallest:
                smallest=current.data
            current=current.next

        return smallest

# create a linked list
linked_list = LinkedList()

# append nodes
linked_list.append(90)
linked_list.append(80)
linked_list.append(50)
linked_list.append(60)

smallest = linked_list.find_smallest()
print(smallest)