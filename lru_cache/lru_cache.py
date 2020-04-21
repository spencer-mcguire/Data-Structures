import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.key_values = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # grabs the value associated with the key 
        # moves that key to the end of the order (move to the head of the line (MRU))
        # return none if the key pair doesnt exist in cache
        # return value associated with the key if it does exist
        #print(f"current storage: {self.storage}")
        if key not in self.storage:
            return None

        node = self.storage[key]

        #if the node is at the MRU already just return. else: add it to the front and delete it 
        self.key_values.move_to_front(node)
        return node.value[1]


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # add the key to the cache 
        # the new added gets set to the head (MRU)
        # if cache is at max limit, delete the tail and then add to the head
        # if key already exists overwrite the old value with the new. delete then add?
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)

            return

        if self.size == self.limit:
           val = self.key_values.remove_from_tail()

           del self.storage[val[0]]
           self.size -= 1

        self.key_values.add_to_head((key, value))
        self.storage[key] = self.key_values.head
        self.size += 1