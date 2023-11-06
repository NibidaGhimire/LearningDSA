# reverse linked list
def reverse_linked_list(self):
 
    prev_node = None
    current = self.head
    next_node = current.next
 
    while True:
 
        current.next = prev_node
                
        prev_node = current
        current = next_node
        next_node = next_node.next
                
        if next_node == None:
            current.next = prev_node
            break
 
    self.head = current  