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

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------



def myMergeHelper(node1, node2):


def mymergeTwoLists(list_node1, list_node2):
    head_node = None
    
    list_node1.val
    list_node2.val

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

def print_nodes(headnode):
    to_return = []
    current_node = headnode
    while current_node is not None:
        to_return.append(current_node.val)
        current_node = current_node.next
    return(to_return)

# Definition for singly-linked list.
from mymodules import LinkedLists as myll

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return mymergeTwoLists(l1, l2):


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest


class TestSolution(unittest.TestCase):
    list1 = myll.LinkedList()
    list1.addList([2, 3, 4])
    list2 = myll.LinkedList()
    list2.addList([5, 6, 7])
    headnode = Solution().mergeTwoLists(list1.head, list2.head)
    to_compare = print_nodes(headnode)
    self.assertEqual(to_compare, [2,3,4,5,6,7])

unittest.main()
