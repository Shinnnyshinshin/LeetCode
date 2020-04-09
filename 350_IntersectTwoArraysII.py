#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""

* The trivial python solution uses a Collections counter
* I'll use a dictionary. 

How will it be used? 

1. Loop through the first array and generate a dictionary where the key is the number, and the value is the number of times it appears in list 1
2. Loop through list 2 
    - check if it is in the dictionary
    - if it is, also check if it has a count greater than 0
    - if so then add to results array
    - decrement count by 1
3. return result



"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_intersect(nums1, nums2):
    res = [] # to return
    nums1_dict = {}
    for num in nums1:
        # good way to simplify
        # get() This is something to remember
        nums1_dict[num] = nums1_dict.get(num, 0) + 1
    
    for num in nums2:
        if num in nums1_dict.keys() and nums1_dict[num] > 0:
            res.append(num)
            nums1_dict[num] -= 1
    return res

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return my_intersect(nums1, nums2)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    
    def test_2(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        output = [2, 2]
        self.assertEqual(Solution().intersect(nums1, nums2), output)
unittest.main()
