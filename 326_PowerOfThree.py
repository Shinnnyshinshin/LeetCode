#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given an integer, write a function to determine if it is a power of three.


"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    * I'm just going to do the loop version and move on. 
    * The other mathematical ones are more language specific (JAVA has a mathematical pitfall, and PYTHON has arbitrary length numbers)


    So what does this method do?

    * we are sequentially dividing the number by b while % is 0, and then we return True. If not then false

    One simple way of finding out if a number n is a power of a number b is to keep dividing n by b as long as the remainder is 0. This is because we can write

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_isPowerOfThree(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return my_isPowerOfThree(n)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 27
        ans = True 
        self.assertEqual(Solution().isPowerOfThree(n), ans)

    def test_2(self):
        n = 0
        ans = False
        self.assertEqual(Solution().isPowerOfThree(n), ans)

    def test_3(self):
        n = 9
        ans = True 
        self.assertEqual(Solution().isPowerOfThree(n), ans)


    def test_4(self):
        n = 45 
        ans = False 
        self.assertEqual(Solution().isPowerOfThree(n), ans)


unittest.main()
