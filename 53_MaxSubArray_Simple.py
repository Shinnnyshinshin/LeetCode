#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

"""

* This is somethign very similar to the coin change problem. 
* We are comparing teh current node vs the maximum 
""" 


def my_maxSubarray(nums):
    if not nums:
        return 0 # edge case with empty array
    current_sum = maxSum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        maxSum = max(maxSum, current_sum)
    return maxSum

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return my_maxSubarray(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ans = 6
        self.assertEqual(Solution().maxSubArray(input), ans)
        
unittest.main()
