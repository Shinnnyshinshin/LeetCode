#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

1. I dont want to use the brute-force method, with will run in O(n^2) complexity. This means a nested for-loop is out of the picture
2. I will approach this through the use of a dictionary which will run a look up in O(1) time vs a "is in" operation for an array, which will run in O(n)
3. One edge case that I defintinitely want to handle is when numbers are repeated. This will be taken care of because you are returning indices as well

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

                

def my_twosum(nums, target):
    nums_dict = {value: index for index, value in enumerate(nums)}
    to_return = []
    # the main loop 
    for i in range(len(nums)):
        current_num = nums[i]
        diff = target - current_num
        # is this the O(1) lookup?
        if diff in nums_dict.keys():
            if i is nums_dict[diff]:
                continue
            to_return.append(i)
            to_return.append(nums_dict[diff])
            break

    return sorted(to_return)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums, target):
        return my_twosum(nums, target)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
class TestSolution(unittest.TestCase):

    def test_PromptTest(self):
        target = 13
        nums = [2, 7, 11, 15]
        ans =  [0, 2]
        self.assertEqual(Solution().twoSum(nums, target), ans)
 
    def test_SecondTest(self):
        target = 6
        nums = [3,2,4]
        ans =  [1,2]
        self.assertEqual(Solution().twoSum(nums, target), ans)
 
unittest.main()
