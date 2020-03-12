#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


# Ok so this is one? 


"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

* this is  traversal that counts as we go down? Let's see if we 

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------
def my_maxDepth(node):
    if node is None:
        return 0
    returned = 1 + max(my_maxDepth(node.left), my_maxDepth(node.right))
    return returned
    

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import unittest
from mymodules import BinaryTree as bt
class Solution:
    def maxDepth(self, root):
        return my_maxDepth(root)
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_build(self):
        test_tree = bt.Tree()
        test_tree.insert(10)
        test_tree.insert(5)
        test_tree.insert(1)
        test_tree.insert(6)
        test_tree.insert(15)
        test_tree.insert(11)
        test_tree.insert(18)
        test_tree.printtree(test_tree.root)
        print(Solution().maxDepth(test_tree.root))
        #self.assertEqual(int(string), ans)
        #self.assertTrue(ans == 1)
        #self.assertFalse(ans == 2)
        
unittest.main()
