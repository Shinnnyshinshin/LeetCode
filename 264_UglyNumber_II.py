#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Share
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
So this is the dynamic program solution : we are going to build an array that stores the first 1670 solutions. and then we can query the index, and then we can . 


How does this sequence proceed?


1, 2, 3, 4, 5, ... 1690

there are 3 indices : i2, i3, i5: we are taking the previous factor.. and mulitplying by 2 or 3 or 5. 
"""

#-------------------------------------------------------------------------------
#    Solution : DynamicProgramming.
#-------------------------------------------------------------------------------

# we are going to store them all and then we are going to 


#-------------------------------------------------------------------------------
#    Solution : Iterative. 
#-------------------------------------------------------------------------------

global ugly_array
ugly_array = []
  
def initialize_ugly_array(max=1690):
    # all zeros
    ugly_array = [0] * max
    # 1 is the first ugly number
    ugly_array[0] = 1

    # indices are being initialized
    ind_2 = ind_3 = ind_5 = 0
    
    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for index in range(1, max):
        ugly_array[index] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) # finding the minumum 

        if ugly_array[index] == next_multiple_of_2:
            ind_2 += 1
            next_multiple_of_2 = ugly_array[ind_2] * 2

        if ugly_array[index] == next_multiple_of_3:
            ind_3 += 1
            next_multiple_of_3 = ugly_array[ind_3] * 3

        if ugly_array[index] == next_multiple_of_5:
            ind_5 += 1
            next_multiple_of_5 = ugly_array[ind_5] * 5
    return ugly_array


def my_isUgly_DP(position_of_ugly):
    if len(ugly_array) is 0:
        my_array = initialize_ugly_array()
        # index of ugly is offset by 1
    return(my_array[position_of_ugly-1]) 


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return my_isUgly_DP(n)
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
class TestSolution(unittest.TestCase):
    def test_5(self):
        self.assertEqual(Solution().isUgly(6), 6)

    def test_6(self):
        self.assertEqual(Solution().isUgly(7), 8)

    def test_150(self):
        self.assertEqual(Solution().isUgly(150), 5832)
        
unittest.main()
