#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    * There are a few ways to do this, but I want to do the Dynamic Programming approach 
    * If you start off from 0 then you have 0 ways 
    * Then you have 1 way for 1 
    * And 2 ways for 2. 

    * the remaining are the sum of index n-1 and n-2
    [  0  1  2  3  4  5  6  ] = these are the indices
    [  0  1  2  3  5  8  13 ] = these are the answers
"""
#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_climbStairs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = [None] * (n+1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    if n > 2:
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
    return(memo[n])
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return my_climbStairs(n)
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_0(self):
        input = 0 
        ans = 0 
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_1(self):
        input = 1
        ans = 1
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_2(self):
        input = 2
        ans = 2
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_3(self):
        input = 3
        ans = 3
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_4(self):
        input = 4
        ans = 5
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_5(self):
        input = 5
        ans = 8
        self.assertEqual(Solution().climbStairs(input), ans)

    def test_6(self):
        input = 6
        ans = 13
        self.assertEqual(Solution().climbStairs(input), ans)


unittest.main()
