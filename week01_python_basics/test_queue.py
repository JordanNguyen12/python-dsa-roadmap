from queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def populated_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


class TestQueue:

    def test_enqueue(self, empty_queue, populated_queue):
        empty_queue.enqueue(1)
        assert empty_queue.front() == 1
        populated_queue.enqueue(4)
        assert populated_queue.last() == 4

    def test_dequeue_fail(self, empty_queue):
        with pytest.raises(IndexError):
            empty_queue.dequeue()

    def test_dequeue(self, populated_queue):
        assert populated_queue.dequeue() == 1
        assert populated_queue.front() == 2

    def test_front_fail(self, empty_queue):
        with pytest.raises(IndexError):
            empty_queue.front()

    def test_front(self, populated_queue):
        assert populated_queue.front() == 1

    def test_last_fail(self, empty_queue):
        with pytest.raises(IndexError):
            empty_queue.last()

    def test_last(self, populated_queue):
        assert populated_queue.last() == 3

    def test_is_empty_fail(self, populated_queue):
        assert populated_queue.is_empty() == False

    def test_is_empty(self, empty_queue):
        assert empty_queue.is_empty() == True
