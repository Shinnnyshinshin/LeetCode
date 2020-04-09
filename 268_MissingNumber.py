#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1] 
Output: 2
Example 2:


Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    Gauss formulation : 
        * Since this is a sequence from 0 to n, we can do this by the length of the array

        Input: [3,0,1] 
        Output: 2

        length = 3
        expected sum = 1 + 2 + 3 = 6
        actual sum = 4



"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_missingNumber(nums):
    expected_sum = (len(nums) * (len(nums) + 1))//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return my_missingNumber(nums)
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        input = [3, 0, 1]
        output = 2
        self.assertEqual(Solution().missingNumber(input), output)

    def test_2(self):
        input = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        output = 8 
        self.assertEqual(Solution().missingNumber(input), output)
      
unittest.main()
