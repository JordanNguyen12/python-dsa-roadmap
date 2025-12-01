from linked_list import LinkedList
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def populated_list():
    ll = LinkedList()
    ll.insert_front(0)
    ll.insert_front(1)
    ll.insert_front(2)
    ll.insert_front(3)
    return ll


class TestLinkedList:

    def test_insert_front(self, empty_list):
        assert empty_list.head is None
        empty_list.insert_front(0)
        assert empty_list.head.value == 0

    def test_insert_multiple_front(selfs, populated_list):
        assert populated_list.head.value == 3
        populated_list.insert_front(4)
        assert populated_list.head.value == 4
        assert populated_list.head.next.value == 3

    def test_insert_end(self, empty_list, populated_list):
        # inserting empty list
        assert empty_list.head is None
        empty_list.insert_end(0)
        assert empty_list.head.value == 0

        # inserting populated list
        current = populated_list.head
        populated_list.insert_end(4)
        while current.next is not None:
            current = current.next
        assert current.value == 4

    def test_delete_at_fail(self, populated_list):
        with pytest.raises(IndexError):
            populated_list.delete_at(9)
            populated_list.delete_at(-1)

    def test_delete_at_pass(self, populated_list):
        # deleting head
        populated_list.delete_at(0)
        assert populated_list.head.next.value == 1
        populated_list.display()
        populated_list.delete_at(1)
        populated_list.display()
        assert populated_list.head.next.value == 0

    def test_get_length(self, empty_list, populated_list):
        assert empty_list.get_length() == 0
        assert populated_list.get_length() == 4

    def test_search(self, populated_list):
        assert populated_list.search(10) == False
        assert populated_list.search(0) == True

    def test_delete_value(self, empty_list, populated_list):
        assert empty_list.delete_value(0) == None
        populated_list.delete_value(3)
        populated_list.display()
        assert populated_list.head.value == 2
        populated_list.delete_value(1)
        assert populated_list.head.next.value == 0



