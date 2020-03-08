#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
create dict. 

* not in dict, then add
* if in dict, then remove
* 1 remaining number returned

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def mysingleNumber(nums):
    my_hashmap = {}
    
    for num in nums:
        if num not in my_hashmap.keys():
            my_hashmap[num] = '1'
        else:
            del my_hashmap[num]
    return([*my_hashmap])

                

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return mysingleNumber(nums)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), [1])

    def test_2(self):
        self.assertEqual(Solution().singleNumber([4, 1, 2, 1, 2]), [4])

unittest.main()
