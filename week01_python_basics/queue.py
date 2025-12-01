class Queue:
    """
    Queue implemented using Python list.
    """

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if self.data:
            return self.data[0]
        else:
            raise IndexError("Queue is empty")

    def last(self):
        if self.data:
            return self.data[-1]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self) -> bool:
        return len(self.data) == 0

'''
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.front())
print(q.last())
'''

