def is_palindrome(self):
    if self.is_empty():
        return False
    
    start = self.head
    end = self.tail
 
    while start != end and start.prev != end:
        if start.data != end.data:
            return False
        start = start.next
        end = end.prev
        
    if(start == end or start == end.next):
        return True
