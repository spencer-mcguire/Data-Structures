import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque


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

    """def depth_first_iterative_for_each(self, cb):
        stack = []
    # add the root of the tree to the stack 
    stack.append(self)
​
    # loop so long as the stack still has elements 
        while len(stack) > 0:
            current_node = stack.pop()
      # check if the right child exists
            if current_node.right:
        stack.append(current_node.right)
      # check if the left child exists
            if current_node.left:
                tack.append(current_node.left)
            cb(current_node.value)"""

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack 
        # breadth-first : queue
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # needs to be a queue FIFO
        # create my queue
        q = Queue()
        # add the node to the queue
        q.enqueue(node)
        # loop the tree as long as the tree exists > 0
        while q.size > 0:
        # set current node to the left most node and delete it using popleft() ( This function is used to delete an argument from the left end of deque)  
            current = q.dequeue()      
        # conditionals:
        # if current exists, print current
            if current:
                print(current.value)
        # if that current node has a left - append it to the queue
            if current.left:
                q.enqueue(current.left)
        # if it has a right - append it to the queue.
            if current.right:
                q.enqueue(current.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # dft = stack
        # create my stack 
        s = Stack()
        #push the node and start the loop
        s.push(node)

        while s.size > 0:
        # remove from the stack, and make it the current node
            current = s.pop()
            # if there is a current, print it
            if current:
                print(current.value)
            # if the is a left, add it to the stack,
            if current.left:
                s.push(current.left)
            # if there is a right, add it to the stack
            if current.right:
                s.push(current.right)




        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)