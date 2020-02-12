#-------------------------------------------------------------------------------
#    Fibonacci Number
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/fibonacci-number/
# Completed 2/11/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Check if input is 0 or 1
2. Recursively add numbers together
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_fib(target: int) -> int:
    if target <= 1:
        return target
    return my_fib(target - 1) + my_fib(target - 2)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def fib(self, N: int) -> int:
        return my_fib(N)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_first(self):
        target = 0
        ans = 0
        self.assertEqual(my_fib(target), ans)
    def test_1(self):
        target = 1
        ans = 1
        self.assertEqual(my_fib(target), ans)
    def test_2(self):
        target = 2
        ans = 1
        self.assertEqual(my_fib(target), ans)  
    def test_20(self):
        target = 20
        ans = 6765
        self.assertEqual(my_fib(target), ans)    
        
unittest.main()
