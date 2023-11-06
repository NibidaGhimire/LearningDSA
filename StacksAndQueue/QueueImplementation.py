class Queue:
    def __init__(self):
        self.queue = []
 
    def enqueue(self, item):
        self.queue.append(item)
 
    def dequeue(self):
        self.queue.pop(0)
 
    def print_queue(self, message):
        print(f"{message}: {self.queue}")


    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if not queue1.is_empty():
            return self.queue[0]



 
queue1 = Queue()
 

queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(100)
 
queue1.print_queue("Queue after adding 3 elements")
 
queue1.dequeue()
 
queue1.print_queue("After removing an item")
 
queue1.dequeue()
 
queue1.print_queue("After removing another item")