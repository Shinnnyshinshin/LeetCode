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

# Function to merge two sorted linked list.
"""mymergeTwoLists(list_node1, list_node2):
    merged_head = None
    merged_tail = None
    list1_head = list_node1
    list2_head = list_node2
    
    if list_node1.val < list_node2.val:        
        merged_head = list_node1
        merged_head.next = list_node2
        merged_tail = list_node2
        # advance
        list1_head = list_node1.next
    else:
        merged_head = list_node2
        merged_head.next = list_node1
        merged_tail = list_node1
        # advance
        list2_head = list_node2.next
    print(print_nodes(merged_head))

    while list1_head or list2_head:
        if list1_head.val < list2_head.val:
            merged_tail.next = list_node1
            merged_tail = list_node1
            list_node1 = list_node1.next
        else: 
            merged_tail.next = list_node2
            merged_tail = list_node2
            list_node2 = list_node2.next
    print(print_nodes(merged_head))

# Function to merge two sorted linked list. 
def mergeLists(head1, head2): 
  
    # create a temp node NULL 
    temp = None
  
    # List1 is empty then return List2 
    if head1 is None: 
        return head2 
  
    # if List2 is empty then return List1 
    if head2 is None: 
        return head1 
  
    # If List1's data is smaller or 
    # equal to List2's data 
    if head1.data <= head2.data: 
  
        # assign temp to List1's data 
        temp = head1 
  
        # Again check List1's data is smaller or equal List2's  
        # data and call mergeLists function. 
        temp.next = mergeLists(head1.next, head2) 
          
    else: 
        # If List2's data is greater than or equal List1's  
        # data assign temp to head2 
        temp = head2 
  
        # Again check List2's data is greater or equal List's 
        # data and call mergeLists function. 
        temp.next = mergeLists(head1, head2.next) 
  
    # return the temp list. 
    return temp 
    """
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


def mergeLists(head1, head2):
    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if head1 is None:
        return head2

    # if List2 is empty then return List1
    if head2 is None:
        return head1

    # If List1's data is smaller or
    # equal to List2's data
    if head1.val <= head2.val:

        # assign temp to List1's data
        temp = head1

        # Again check List1's data is smaller or equal List2's
        # data and call mergeLists function.
        temp.next = mergeLists(head1.next, head2)

    else:
        # If List2's data is greater than or equal List1's
        # data assign temp to head2
        temp = head2
        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeLists(head1, head2.next)

    # return the temp list.
    return temp

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
        return mergeLists(l1, l2)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
class TestSolution(unittest.TestCase):
    def test_6(self):

        list1 = myll.LinkedList()
        list1.addList([2, 3, 4])
        list2 = myll.LinkedList()
        list2.addList([5, 6, 7])
        headnode = Solution().mergeTwoLists(list1.head, list2.head)
        to_compare = print_nodes(headnode)
        print(to_compare)
        self.assertEqual(to_compare, [2,3,4,5,6,7])

unittest.main()
