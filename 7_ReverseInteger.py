#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

* The easiest way to do this would be convert to a string, and then reverse and make sure it has the correct sign. 
* If there 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def checkoverflow(num_to_check, is_neg):
    mymax = 2**31 - 1
    mymin = -2**31
    if is_neg:
        num_to_check *= -1
        if num_to_check < mymin:
            print(num_to_check)
            num_to_check = 0
    else:
        if num_to_check > mymax:
            num_to_check = 0
    return(num_to_check)


def myreverse(num_to_reverse):
    str_to_return = ""
    is_neg = False
    
    split_as_string = list(str(num_to_reverse))
    end_ind = 0

    if split_as_string[0] is '-':
        is_neg = True
        end_ind = 1 # end one before the beginning
    for ind in reversed(range(end_ind, len(split_as_string))):
        str_to_return += split_as_string[ind]
    
    num_to_return = int(str_to_return) 
    
    # check overflow 
    num_to_return = checkoverflow(num_to_return, is_neg)
    return(num_to_return)



#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        """
        return myreverse(x)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
import sys

class TestSolution(unittest.TestCase):

    def test_123(self):
        self.assertEqual(Solution().reverse(123), 321)

    def test_neg123(self):
        self.assertEqual(Solution().reverse(-123), -321)

    def test_120(self):
        self.assertEqual(Solution().reverse(120), 21)

    def test_overflow(self):
        self.assertEqual(Solution().reverse(1534236469), 0)

unittest.main()
