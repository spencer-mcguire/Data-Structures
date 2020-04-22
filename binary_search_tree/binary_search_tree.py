import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # does not return anything 
    def insert(self, value):
        # self.left or right need to be valid nodes to call insert on them
        if value < self.value:
            # check if self.left is valid node
            if self.left:
                self.left.insert(value)
            # left side is empty
            else:
                self.left = BinarySearchTree(value)
        else:
            # value is > self.value
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

                
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #search the tree for the target 
        # if the target is less than self go to the left
        # if target is greater than self go to the right
        # continue until either no nodes left or your find the target 
        # return true if found
        # return false if not found
        #print(f'I am the target:{target}')
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            # if > than
            if self.right:
                return self.right.contains(target)
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        # need to return the max value in the tree
        # if node exists loop again until loop doesnt exist
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # every time we loop call the cb with the value of the node
        # check if left exists, if it does call for_each again
        # check if right exists, if it does call for each again
        # 
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
