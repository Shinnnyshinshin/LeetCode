#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    My initial assumption is that this is going to be similar to permutations (Leetcode #46)

    * Permutations you have N! possibilities, 
    * Subsets are a little bit different 
            - mathematically they are defined by 2^N 
            - because each element can either be present or non-present
            
    * Ok so Knuth has a really really good way of doing this 
    * you are basically going through all the combination of bits from 000 to 111 and using that to keep or leave an item out

    * how do you get rid of the problem of '0' padding? 
    * you just start at a later number

    * if you need 3 0's (000)
    * then you just start at (1000) and take a substring that ignores that first 1
 
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]


"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_subsets(nums):
    n = len(nums)
    output = []
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]

        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    return output

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return my_subsets(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        nums = [1, 2, 3]
        ans = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
        self.assertEqual(Solution().subsets(nums), ans)
        
unittest.main()
