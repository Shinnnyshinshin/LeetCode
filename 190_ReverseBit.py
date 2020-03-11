#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""

Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 


"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

* Python has a binary reperesntation bin(10) which will return a binary representation of a number
    - for instance bin(10) = 0b1010
* we will take just the 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_reverseBits(n):
    bitsize = 32 
    # in the case of 43261596
    mybin = bin(n)  # 0b10100101000001111010011100
    reversed_bin = mybin[-1:1:-1]  # 10100101000001111010011100
    # this means you start at the end, and come town to 1(not inclusive), and decrement by -1 each time. 
    # we need to fill in the rest of the number with 0s 
    # before : 00111001011110000010100101
    reversed_bin = reversed_bin + (bitsize - len(reversed_bin)) * '0'
    # after : 00111001011110000010100101000000
    return(int(reversed_bin,2))
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def reverseBits(self, n):
        return(my_reverseBits(n))

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    #def test_development(self):
    #    Solution().reverseBits(43261596)
    def test_example1(self):
        self.assertEqual(Solution().reverseBits(43261596), 964176192)

    def test_example2(self):
        self.assertEqual(Solution().reverseBits(4294967293), 3221225471)
        
unittest.main()
