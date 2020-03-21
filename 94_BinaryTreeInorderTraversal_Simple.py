#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_inorderTraversal(root):
    ans = []
    def recurse(r):
        if not r:
            return
        recurse(r.left)
        ans.append(r.val)
        recurse(r.right)
    recurse(root)
    return ans

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def inorderTraversal(self, root):
        return my_inorderTraversal(root)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
from mymodules import BinaryTree as binarytree

class TestSolution(unittest.TestCase):
    def test_example(self):
        string = [1, None, 2, 3]
        # turn this into a tree
        ans = [1, 3, 2]
        self.assertEqual(int(string), ans)
        
unittest.main()
