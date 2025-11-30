class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Singly linked list implementation.
    """

    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_at(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1

        current.next = current.next.next

    def delete_value(self, value):
        if self.get_length() == 0:
            return None

        if self.head.value == value:
            self.head = self.head.next

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            return

        current.next = current.next.next

    def search(self, value) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def display(self):
        # Helper: print all nodes
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("null")