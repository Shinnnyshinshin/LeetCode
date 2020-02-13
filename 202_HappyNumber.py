#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. The first approach will involve splitting 
2. version 2 will look at modulo for getting the number the algorithm will work like this

sum = 0
num = 169
while num > 0:
    first number : num % 10 (which is 9)
    sum += first number ^2
    num = num / 10
we can check whether this is a happy number

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

              
class MySolution:
    def __init__(self):
        self.solutions = []
    def isHappy(self, n):
        if (n is 1):
            return True
        elif n in self.solutions:
            print("n is " + str(n))
            print("is in set" + str(self.solutions))
            return False
        else:
            self.solutions.append(n)
            # first split into the digits
            res = [int(x) for x in str(n)]
            
            mysum = 0 
            for x in res:
                mysum += x**2
            return self.isHappy(mysum)
           

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution:
    def isHappy(self, n):
        return MySolution().isHappy(n)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        input = 19
        ans = True
        self.assertEqual(Solution().isHappy(input), ans)
        
unittest.main()
