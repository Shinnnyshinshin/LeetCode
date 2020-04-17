#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def my_reverseList_helper(previous_node, current_node):
    if current_node.next == None:
        current_node.next = previous_node
        return current_node
    
    next_node = current_node.next
    current_node.next = previous_node
    return my_reverseList_helper(current_node, next_node)



def my_reverseList(head):
    # return if empty
    if head is None:
        return
    # recursion begins
    new_head = my_reverseList_helper(None, head)
    return(new_head)
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        return my_reverseList(head)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
from mymodules import LinkedLists as linked
class TestSolution(unittest.TestCase):
    def test_simple(self):
        my_ll = linked.LinkedList()
        my_ll.addList([1,2,3,4,5])
        reversed_list = [5, 4, 3, 2, 1]
        returned = Solution().reverseList(my_ll.head)
        returned_ll = linked.LinkedList(head = returned)
        self.assertEqual(returned_ll.printList(), reversed_list)


unittest.main()
