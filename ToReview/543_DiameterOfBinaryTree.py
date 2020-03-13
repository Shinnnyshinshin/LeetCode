#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \    
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. The way that we can approach this is this. For each node, we can calculate that the diameter at each node is the number of nodes in left subtree-path + right subtree-path + 1(the current node)
2. 

self.ans = 0
def depth(root):
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            # path
            self.ans = max(self.ans, left + right)
            # depth
            return max(left, right) + 1
 depth(root)
 return self.ans

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


#def _mydiameterOfBinaryTree_helper(node):
#    if node is None:
#        return 0
global ans
ans = 0

def mydiameterOfBinaryTree(node):
    if node is None:
        return 0 
    to_return_left = mydiameterOfBinaryTree(node.left)
    to_return_right = mydiameterOfBinaryTree(node.right)

    global ans
    ans = max(ans, to_return_left + to_return_right)
    return(max(to_return_left, to_return_right) + 1)
    

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        global ans
        mydiameterOfBinaryTree(root)
        return ans

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
from mymodules import BinaryTree as bt

class TestSolution(unittest.TestCase):

    def test_solution(self):
        test_tree = bt.Tree()
        test_tree.insert(10)
        test_tree.insert(5)
        test_tree.insert(1)
        test_tree.insert(6)
        test_tree.insert(15)
        test_tree.insert(11)
        test_tree.insert(18)
        test_tree.printtree(test_tree.root)
        self.assertEquals(Solution().diameterOfBinaryTree(test_tree.root), 4)

    def test_empty(self):
        self.assertEquals(Solution().diameterOfBinaryTree(bt.Tree().root), 0)

unittest.main()
