#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Do a binary search on the mid of the number, and then we can do a check, and then go down or up from there. 

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def mymySqrt(x):
    
    # these are the base cases
    if x is 0 or x is 1:
        return x
    
    # do a binary search for  the floor of sqrt(x)
    start = 1
    end = x // 2
    answer = None

    while start <= end:
        mid = (start + end)//2 # for the integer value
        sqr = mid * mid
        if sqr is x:
            answer = int(mid)
            break # we are already there
        
        elif sqr <= x:
            # get rid of left search space
            start = mid + 1
            answer = int(mid)
        else:
            # get rid of right search space
            end = mid - 1

    return answer


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return (mymySqrt(x))


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_4(self):
        self.assertEqual(Solution().mySqrt(4), 2)

    def test_3(self):
        self.assertEqual(Solution().mySqrt(9), 3)

    def test_8(self):
        self.assertEqual(Solution().mySqrt(8), 2)

    def test_1034(self):
        self.assertEqual(Solution().mySqrt(1024), 32)
unittest.main()
