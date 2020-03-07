"""

Implementation of Linked List in python

LinkedLists.py is a simple implementation of Linked List in python.
Following are the methods implemented

push, reverse, printlist

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def set_next(self, nextval):
        self.next = nextval


class LinkedList:
    # initialize the head
    def __init__(self):
        self.head = None
    def push(self, new_val):
        # to the beginning
        newNode = ListNode(new_val)
        newNode.next = self.head
        self.head = newNode
    def append(self, new_val):
        lastNode = self.head
        if self.head is None:
            self.push(new_val)
        else:
            while lastNode.next is not None:
                lastNode = lastNode.next
            newNode = ListNode(new_val)
            lastNode.next = newNode

    def helper_function_for_switch(self, previous_node, current_node):
        # what is our finishing function
        # if there is no more node
        if current_node.next == None:
            self.head = current_node
            # mark it done
            current_node.next = previous_node
            return
    
        next_node = current_node.next
        current_node.next = previous_node
        self.helper_function_for_switch(current_node, next_node)        
    def reverse(self):
        if self.head is None:
            return
        self.helper_function_for_switch(None, self.head)
    def addList(self, listToAdd):
        for item in listToAdd:
            self.append(item)
    
    def printList(self):
        to_return = []
        current_node = self.head
        while current_node is not None:
            to_return.append(current_node.val)
            current_node = current_node.next

        return(to_return)

"""
global MyList
MyList = LinkedList()
MyList.push(5)
MyList.push(4)
MyList.push(3)
MyList.push(2)
MyList.push(1)

MyList.printList()
MyList.reverse()
MyList.printList()

"""
