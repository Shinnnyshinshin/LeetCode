#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
 * there are a few special cases: 
    - carrying the 1
    - carrying the one to the beginning of the array

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def myplusOne(digits):
    # first we add 1 to the end 
    digits[-1] = digits[-1] + 1
    
    # then we loop backwards and since reversed returns a tuple, we are just dumping it
    for index, _ in reversed(list(enumerate(digits))):
        if digits[index] > 9:
            # then we have to carry
            digits[index] = 0
            if index != 0:
                digits[index-1] += 1
        
            else:
                digits = [1]+digits
        else:
            continue
    return digits

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution:
    def plusOne(self, digits):
        return myplusOne(digits)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        input = [1, 2, 3]
        ans = [1, 2 , 4]
        self.assertEqual(Solution().plusOne(input), ans)
    
    def test_99(self):
        input = [9, 9]
        ans = [1, 0, 0]
        self.assertEqual(Solution().plusOne(input), ans)

unittest.main()
