def reverse_elements(self):
    values = []
    current = self.head
    while current:
        values.append(current.data)
        current = current.next
    
    current = self.head
    for value in reversed(values):
        current.data = value
        current = current.next   