#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    I'll try to solve this problem using an extra array. It would still be
    O(n) space, and O(n) run time since we are looping through input array once

    Ho 
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_rotate(nums, k):
    pass
                

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return my_rotate(nums, k)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        input = [-1, -100, 3, 99]
        k = 3
        solution = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(Solution().rotate(input, k), solution)
        
    def test_2(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solution = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(Solution().rotate(input, k), solution)

unittest.main()
