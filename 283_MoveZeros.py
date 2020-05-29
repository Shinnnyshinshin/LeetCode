#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
# LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Can I just do the easy version?

loop through 
    list.remove(i)
    list.append(0)

But no, we are better than that. I'll use the 2-pointer
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def mymoveZeros(nums):
    # we are going to store a value that has the 
    last_ind_non_zero = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            # move to last ind of nonZero
            nums[last_ind_non_zero] = nums[index]
            last_ind_non_zero += 1

    # fill the rest as 0's
    for index in range(last_ind_non_zero, len(nums)):
        nums[index] = 0
    return(nums)
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        return(mymoveZeros(nums))

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        input_array = [0, 1, 0, 3, 12]
        ans_array = [1, 3, 12, 0, 0]
        self.assertEqual(Solution().moveZeroes(input_array), ans_array)
        
unittest.main()
