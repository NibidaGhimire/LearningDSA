class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not stack1.is_empty():
            self.stack.pop()

    def peek(self):
        if not stack1.is_empty():
            return self.stack[-1]

    def print_stack(self, message):
        print(f"{message}: {self.stack}")

stack1 = Stack()

stack1.push(5)
stack1.push(100)
stack1.push(1000)

stack1.print_stack("Stack after pushing 2 items")

print(f"Peek the stack: {stack1.peek()}")

stack1.print_stack("Stack after peeking")

stack1.pop()

stack1.print_stack("After popping")



#Time Complexity : O(n)