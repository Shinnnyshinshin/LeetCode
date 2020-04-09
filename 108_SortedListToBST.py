#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    This should be pretty straight forward. A few things to do think about though: 

    * since it is a sorted list, we can take the mid-point, and then create a smaller subtree, and then keep going
    *     

     
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from mymodules import BinaryTree as bt
def my_sortedArrayToBST(nums):
    pass

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return my_sortedArrayToBST(nums)
      
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
from mymodules import BinaryTree  as bt

class TestSolution(unittest.TestCase):

    def test_solution(self):
        test_tree = bt.Tree()
        test_tree.insert(0)
        # left
        test_tree.insert(-3)
        test_tree.insert(-10)
        # right
        test_tree.insert(9)
        test_tree.insert(5)
        test_tree.printtree(test_tree.root)
        #self.assertEquals(Solution().diameterOfBinaryTree(test_tree.root), 4)

        
unittest.main()
