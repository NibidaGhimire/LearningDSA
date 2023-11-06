def search(self, value):
        if self.node_count()==0:
            return False
        
        current=self.head
        while True:
            current=current.next
            if current.data==value:
                return True
           
            if current==self.head:
                break
        
        return False