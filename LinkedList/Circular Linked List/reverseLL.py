def reverse(self):
    if self.node_count() < 2:
        return
    
    prev = None
    current = self.head
    next_node = current.next
    
    while True:
        
        
        current.next = prev
        
        prev = current
        current = next_node
        next_node = current.next
        
        if current == self.head:
            break
    
    
    self.head.next = prev
    self.head = prev  