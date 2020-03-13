#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#  
# 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

"""


#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------
"""
* This question is harder to set up to unittest than it is to solve. 

* [1]->[2]->[3]->[4]->[5]->None

If we were going to delete [3], then we are just going replace it with the next one and just... leave the original [4] hanging

* [4]-->[5] The original 4 node still pointing to 5
* [1]-->[2]-->[4]-->[5]-->None. The new list with the '3' deleted
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


import unittest
from mymodules import LinkedLists as linked

global global_list

def my_deleteNode(current_node):
    # delete the following one
    if current_node is None:
        return
    # set the thing
    else:
        if current_node.next is not None:
            current_node.val = current_node.next.val
            current_node.next = current_node.next.next

        else:
            current_node = None

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        return my_deleteNode(node)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------



class TestSolution(unittest.TestCase):

   def test_simple(self):
        my_ll = linked.LinkedList()
        my_ll.addList([1, 2, 3, 4, 5])
        global global_list
        global_list = my_ll # make sure it deltes
        # return 
        deleted_list = linked.LinkedList()
        deleted_list.addList([1, 2, 4, 5])
        # Delete operation
        node_to_delete = my_ll.head.next.next # 3
        Solution().deleteNode(node_to_delete) # actual funcitno call
        self.assertEqual(global_list.printList(), deleted_list.printList())


unittest.main()
