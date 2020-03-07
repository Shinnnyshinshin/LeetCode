#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

from mymodules import LinkedLists as myll

def my_two_sum_helper(node1, node2, carryover):
    mysum = carryover
    if node1:
        mysum += node1.val
    if node2:
        mysum += node2.val
    return(mysum)


def my_twosum(list1_current, list2_current):
    carryover = 0
    head_node = None
    current_node = None
    # keep doing while the nodes are all valid

    returned = my_two_sum_helper(list1_current, list2_current, carryover)
    while returned is not 0:
        to_add = returned % 10
        carryover = returned // 10
        if head_node is None:
            head_node = myll.ListNode(to_add)
            current_node = head_node
        else:
            current_node.next = myll.ListNode(to_add)
            current_node = current_node.next

        if list1_current is not None:
            list1_current = list1_current.next
        if list2_current is not None:
            list2_current = list2_current.next
        returned = my_two_sum_helper(list1_current, list2_current, carryover)

    return(head_node)
                

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return my_twosum(l1, l2)



#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_Example(self):
        list1 = myll.LinkedList()
        list1.append(2)
        list1.append(4)
        list1.append(3)

        list2 = myll.LinkedList()
        list2.append(5)
        list2.append(6)
        list2.append(4)


        self.assertEqual(Solution().addTwoNumbers(list1.head, list2.head), )
        
unittest.main()
[2,4,3]
[5,6,4]