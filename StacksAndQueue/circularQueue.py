# create class to represent a circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0 
        self.count = 0 
 
    
    def is_full(self):
        return self.count == self.size
 
   
    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            return
        index = (self.front + self.count) % self.size
        self.queue[index] = item
        self.count += 1
 
   
    def dequeue(self):
        if self.is_empty():
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
 
    def print_queue(self, message):
        print(f"{message}: {self.queue}")
 

queue1 = CircularQueue(4)
 

queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(100)
queue1.print_queue("Queue after adding 3 elements")
 
queue1.dequeue()
queue1.print_queue("After removing an item")
 

queue1.enqueue(150)
queue1.enqueue(200)
queue1.print_queue("After adding two more items")
 

queue1.enqueue(250)