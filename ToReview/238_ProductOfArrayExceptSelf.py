#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    The simplest approach would be to multiply everything, and then fill the array with total / number at current index. But leetcode says don't do that

    * So what would be the next way to do it? 
    * Is it possible to have 2 more arrays, where the number
    
    - forward[]
    - backward[]
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

                
def my_productExceptSelf(nums):

    # The length of the input array
    length = len(nums)

    # The left and right arrays as described in the algorithm
    L, R, answer = [0]*length, [0]*length, [0]*length

    # L[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the L[0] would be 1
    L[0] = 1
    for i in range(1, length):
        # L[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all
        # elements to the left of index 'i'
        L[i] = nums[i - 1] * L[i - 1]
    
    # R[i] contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R[length - 1] would be 1
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        # R[i + 1] already contains the product of elements to the right of 'i + 1'
        # Simply multiplying it with nums[i + 1] would give the product of all
        # elements to the right of index 'i'
        R[i] = nums[i + 1] * R[i + 1]
    # Constructing the answer array
    for i in range(length):
        # For the first element, R[i] would be product except self
        # For the last element of the array, product except self would be L[i]
        # Else, multiple product of all elements to the left and to the right
        answer[i] = L[i] * R[i]
    return(answer)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return my_productExceptSelf(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_s(self):
        input = [1, 2, 3, 4]
        output = [24, 12, 8, 6] 
        self.assertEqual(Solution().productExceptSelf(input), output)
        
unittest.main()
