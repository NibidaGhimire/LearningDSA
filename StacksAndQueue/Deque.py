
class Deque:
    def __init__(self):
        self.deque = []

    def add_rear(self,item):
        self.deque.append(item)

    def add_front(self,item):
        self.deque.insert(0,item)

    def remove_front(self):
        self.deque.pop(0)

    def remove_rear(self):
        self.deque.pop()
        
    def print_queue(self):
        print(self.deque)

d = Deque()

input_str = input()

number1, number2, number3, number4 = [int(val) for val in input_str.split()]

d.add_rear(number1)
d.add_rear(number2)
d.print_queue()

d.add_front(number3)
d.add_front(number4)
d.print_queue()

d.remove_rear()
d.print_queue()

d.remove_front()
d.print_queue()