#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
global full
full = []
def my_permute_helper(my_nums, start, end):
    if start == end:
        full.append(my_nums)
        print(my_nums)
        return 
    else:
        for i in list(range(start, end+1)):
            my_nums[start], my_nums[i] = my_nums[i], my_nums[start]
            my_permute_helper(my_nums, start + 1, end)
            my_nums[start], my_nums[i] = my_nums[i], my_nums[start]
def my_permute(nums):
    my_permute_helper(nums, 0, len(nums)-1)
    #print(full)
    return full
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


class Solution:
    def permute(self, nums):
        return my_permute(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_123(self):
        string = [1,2,3]
        ans = [[1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]]
        self.assertEqual(Solution().permute(string), ans)
unittest.main()
