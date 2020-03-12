#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Storing values in dictionary. and seeing if number exists as key. If at any point you reach a number that already in dict, return true. Else return false. 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def mycontainsDuplicate(nums):
    dups = {}
    for num in nums:
        if num in dups.keys():
            return True
        dups[num] = 1
    return False

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums):
        return mycontainsDuplicate(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        list_of_num = [1, 2, 3, 1]
        self.assertTrue(Solution().containsDuplicate(list_of_num))

    def test_2(self):
        list_of_num = [1, 2, 3, 4]
        self.assertFalse(Solution().containsDuplicate(list_of_num))

    def test_3(self):
        list_of_num = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(Solution().containsDuplicate(list_of_num))

unittest.main()

