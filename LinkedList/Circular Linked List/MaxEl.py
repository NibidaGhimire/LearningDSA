def find_max(self):
   
    if self.is_empty():
        return None

    current = self.head
   
    maximum= current.data
    while True:
      
        current = current.next
        if current.data > maximum:
            maximum = current.data
        
        if current is self.head:
            break
    
    return maximum
