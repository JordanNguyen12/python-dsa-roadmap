class Stack:
    """
    Stack implemented using Python list.
    """

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

'''
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
'''



