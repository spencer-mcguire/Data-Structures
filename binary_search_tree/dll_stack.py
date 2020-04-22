import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? stack opperates on FIFO just good practice
        self.storage = DoublyLinkedList()

    def push(self, value):
        # like append add to the tail
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def pop(self):
        # remove from the tail or return none if empty 
        if self.size == 0:
            return None
        removed = self.storage.remove_from_tail()
        self.size = self.storage.length
        return removed

    def len(self):
        return self.size
