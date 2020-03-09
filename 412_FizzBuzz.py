#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

* This just tests for % function
* for the multiple of 3 and 5. 
    - can you be a multiple of 3 and 5 without being a multiple of 5? 
    - 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def myfizzBuzz(n):
    list_to_return = []
    # indices are offset by 1
    for i in range(1, n+1):
        to_add = ''
        if i % 3 is 0:
            to_add += "Fizz"
        if i % 5 is 0:
            to_add += "Buzz"
        if to_add is '':
            to_add += str(i)
        list_to_return.append(to_add)    
    return (list_to_return)
    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return myfizzBuzz(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_15(self):
        ans = ["1","2","Fizz","4","Buzz", "Fizz","7", "8","Fizz", "Buzz", "11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(Solution().fizzBuzz(15), ans)
        
unittest.main()
