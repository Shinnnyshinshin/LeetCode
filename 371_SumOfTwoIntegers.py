#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

* so this is a bitwise operator problem. 

* how does this work? 
* if we do an OR th
    - In Python, bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators.
https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def mygetSum(a,b):
    # how does this work
    while b:
        a, b = (a ^ b), ((a & b) << 1)
    return(a)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution:
    def getSum(self, a, b): 
        return mygetSum(a,b)



#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(Solution().getSum(1,2), 3)

    def test_zero(self):
        self.assertEqual(Solution().getSum(-1, 1), 0)

unittest.main()
