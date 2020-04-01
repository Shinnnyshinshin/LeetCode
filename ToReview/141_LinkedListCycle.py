#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
- So there are 2 classical ways to approach this problem

1. This is to use a HashTable. 
    - For each node that is in the list, you add it to a hashmap
    - you check to see if it is in the hashmap O(1) operation
    - and you are going through the linked list once O(n)
    - so this is pretty efficient, but you need O(n) space. 

2. You can also use 2 pointers. In this way you are using O(1) additional space (just one more node)
    - you are having 2 pointers. 
        - one "fast" one
        - one "slow" one
    - if they ever meet, then you have a looop
    - how do you go about checking this 
    - I can even implement both

- Now to get the implementation of this. That is going to be the tricky part, and that is what I'll try to do this afternoon. 
- 

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


def my_hasCycle_FastSlowPointers(head):
    # if we are the end node, then we return False, there is no loop
    if head is None or head.next is None:
        return False
    
    slow_pointer = head
    fast_pointer = head.next
    while slow_pointer != fast_pointer:
        # we have gotten to the end
        if fast_pointer is None or fast_pointer.next is None:
            return False
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return True 


def my_hasCycle_hashmap(head):
    seen = {}
    while head is not None:
        if head in seen.keys():
            return True
        else:
            seen[head] = 1 
        # keep going
        head = head.next
    return False


# this is my driver for 
def my_hasCycle(head):
    #return my_hasCycle_hashmap(head)
    return my_hasCycle_FastSlowPointers(head)
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return my_hasCycle(head)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------


# build first loop
def build_test1():
    vals = [3, 2, 0, -4]
    node0 = ListNode(vals[0])
    node1 = ListNode(vals[1])
    node2 = ListNode(vals[2])
    node3 = ListNode(vals[3])
    node0.next = node1 
    node1.next = node2
    node2.next = node3
    node3.next = node0
    return node0


def build_test2():
    vals = [1, 2]
    node0 = ListNode(vals[0])
    node1 = ListNode(vals[1])
    node0.next = node1
    node1.next = node0
    return node0

def build_test3():
    vals = [1]
    node0 = ListNode(vals[0])
    return node0

import unittest
class TestSolution(unittest.TestCase):

    def test_1(self):
        nodes = build_test1()        
        res = True 
        self.assertEqual(Solution().hasCycle(nodes), res) 

    def test_2(self):
        nodes = build_test2()
        res = True
        self.assertEqual(Solution().hasCycle(nodes), res)

    def test_3(self):
        nodes = build_test3()
        res = False
        self.assertEqual(Solution().hasCycle(nodes), res)

unittest.main()
