from stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def populated_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


class TestStack:

    def test_push(self, empty_stack, populated_stack):
        empty_stack.push(1)
        assert empty_stack.peek() == 1
        print(empty_stack.peek())
        populated_stack.push(5)
        assert populated_stack.peek() == 5

    def test_pop_fail(self, empty_stack):
        with pytest.raises(IndexError):
            empty_stack.pop()

    def test_pop(self, populated_stack):
        assert populated_stack.pop() == 4

    def test_peek_fail(self, empty_stack):
        with pytest.raises(IndexError):
            empty_stack.peek()

    def test_peek(self, populated_stack):
        assert populated_stack.peek() == 4

    def test_is_empty_fail(self, populated_stack):
        assert populated_stack.is_empty() == False

    def test_is_empty(self, empty_stack):
        assert empty_stack.is_empty() == True