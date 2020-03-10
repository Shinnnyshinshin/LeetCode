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
    https://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python 

* a few preliminary definitions : 

* The algorithm itself has to do with an OR and AND operation on the two integers to calculate the sum initially :

We will use 4 bit integers to simplify the calcuation 

0001 = 1 (A) 
0001 = 1 (B)

In the calculation of A + B, we first do an OR operation
0001 OR 0001  = 0000 

and then we do an AND carrying the 1 with a << 1 operation 
0001 AND 0001 = 0001 
0001 << 1 = 0010

Now we go through a second iteration : 

A = 0000
B = 0010 

A = 0010
B = 0000 

The program returns A, which is 0010 or 2

There are two additional steps that need to be taken since python isn't constrained by 16 or 32 or 128 bit integers.  
This means that for an operation like 1 + (-1) = 0, then it will be stuck in an infinite loop. Because the Python interpreteter will keep on allcating more bits 

- So we want to constrain our calculations. In our case, as 128 bit integers. 
- we do this by performing a MOD operation on the following mask, which is one greater than 0xFFFFFFFF 
- 0x100000000 = MASK

this means anything larger than the mask will just be "reset" to a smaller value within the range 128 bit range the method is designed for. 

The MAX and MIN values serve the same purpose, more specifically to handle negative numbers.. since 
Here in an example with 4 bit integer with the first bit being a signed bit and -x being represented as ~(x-1)

0000 = 0
0001 = 1
0010 = 2
0011 = 3
0100 = 4
0101 = 5
0110 = 6
0111 = 7

and the negative numbers

1000 = -8 (8)
1001 = -7 (9)
1010 = -6 (10)
1011 = -5 (11)
1100 = -4 (12)
1101 = -3 (13)
1110 = -2 (14)
1111 = -1 (15)

as an example, let's add -1 and -2

1110 - a
1111 - b

the first step is an OR
0001 - a is (a ^ b)
1100 - b is (a & b << 1)

next loop
1101 - a is (a ^ b)
0000 - b is (a & b << 1)

returns a = 1101 (13, which is larger than our max int 7...we have an overflow error)

to convert to -3 we do the following steps 

13 % 8 = 5

0101 = is result
0111 = max int
------------ ^ operation
0010
------------ ~ operation
1101  is the final answer (converted into negative value)
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def mygetSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000
    while b:
        a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


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
        self.assertEqual(Solution().getSum(1, 1), 2)

    def test_simple2(self):
        self.assertEqual(Solution().getSum(32, 2), 34)

    def test_simple3(self):
        self.assertEqual(Solution().getSum(100, 2), 102)

    def test_simple4(self):
        self.assertEqual(Solution().getSum(9999, 1), 10000)

    def test_zero(self):
        self.assertEqual(Solution().getSum(-2, 3), 1)

    def test_twoNeg(self):
        self.assertEqual(Solution().getSum(-12, -8), -20)


unittest.main()
