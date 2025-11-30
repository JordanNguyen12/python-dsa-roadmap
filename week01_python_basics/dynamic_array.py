class DynamicArray:
    """
    A lightweight wrapper around Python's built-in list
    to simulate a dynamic array API.
    """

    def __init__(self):
        self.data = []

    def append(self, value):
        """Add element to end."""
        # TODO: Implement
        pass

    def insert(self, index: int, value):
        """Insert element at index."""
        # TODO: Implement
        pass

    def pop(self):
        """Remove last element."""
        # TODO: Implement
        pass

    def get(self, index: int):
        """Get element by index."""
        # TODO: Implement
        pass

    def size(self) -> int:
        """Return the number of elements."""
        return len(self.data)
