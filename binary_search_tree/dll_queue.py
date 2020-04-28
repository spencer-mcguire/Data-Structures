import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? more efficient with an O(1) runtime
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
         # should add an item to the back of the queue
         # call method to place an item at the end of the queue
         self.storage.add_to_tail(value)
         self.size = self.storage.length


    def dequeue(self):
        if self.size == 0:
            return None
        removed = self.storage.remove_from_head()
        self.size = self.storage.length
        return removed

    def len(self):
        return self.size
