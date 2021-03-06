#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Prime factors only include 2, 3, 5
    - is the % of 2, 3, 5 zero.  This is the first condition. 
    - there can't be other prime factors... then you keep dividing it down.. and then you have to be left with 1. If you are left with a number that is not 

* the equation is something like this : u=(2^i)*(3^j)*(5^k)

"""

#-------------------------------------------------------------------------------
#    Solution : DynamicProgramming.
#-------------------------------------------------------------------------------

# we are going to store them all and then we are going to 


#-------------------------------------------------------------------------------
#    Solution : Iterative. 
#-------------------------------------------------------------------------------

def my_isUgly_Iterative(num_to_test):
    if num_to_test <= 0:
        return False
    for p in [2,3,5]:
        while num_to_test % p == 0:
            num_to_test /= p
    return num_to_test == 1

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return my_isUgly_Iterative(num)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
class TestSolution(unittest.TestCase):
    def test_6(self):
        self.assertEqual(Solution().isUgly(6), True)

    def test_8(self):
        self.assertEqual(Solution().isUgly(8), True)

    def test_14(self):
        self.assertEqual(Solution().isUgly(14), False)
        
unittest.main()
