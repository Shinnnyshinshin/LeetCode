#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 
 Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    So first we can do something
    
    The bit-manipulation trick is very interesting. 

    * n & n-1 is going to flip the least significant bit to 0

    For example    
    * 1010 : 10 
    * 1001 : 9

    * 1000 : n
    * 0111 : n-1

    https://leetcode.com/articles/number-1-bits/

    * this is very interesting and very smart
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def myhammingWeight(n):
    num_ones = 0
    # convert the string to binary
    n = int(n, 2)
    while(n > 0):
        num_ones += 1
        n &= (n-1)
    return num_ones

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def hammingWeight(self, n):
        return myhammingWeight(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        string = "00000000000000000000000000001011"
        ans = 3 
        self.assertEqual(Solution().hammingWeight(string), ans) 

    def test_simple2(self):
        string = "00000000000000000000000010000000"
        ans = 1 
        self.assertEqual(Solution().hammingWeight(string), ans)


    def test_simple(self):
        string = "11111111111111111111111111111101"
        ans = 31
        self.assertEqual(Solution().hammingWeight(string), ans)

unittest.main()
