#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""

The first we would need is some sort of way to get the number from the letter. 

That function is ord(), which gives the ASCII code for a letter, so that ord(A) is '65'

You can therefore get the index of the letter by doing 

    ord(letter) - ord('A') + 1 

How do we add the second letter? 

* we can keep adding +26 to the index every time we get a new letter? 

* we also want to reverse the string so that we can go from right to left : 

"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_titleToNumber(string):
    index = 0
    string = string[::-1]
    for exponent, letter in enumerate(string):
        index += (ord(letter) - ord('A') + 1) * (26 ** exponent)
    return index

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return my_titleToNumber(s)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    def test_A(self):
        string = "A"
        ans = 1
        self.assertEqual(Solution().titleToNumber(string), ans)
        
    def test_AB(self):
        string = "AB"
        ans = 28
        self.assertEqual(Solution().titleToNumber(string), ans)

    def test_ZY(self):
        string = "ZY"
        ans = 701
        self.assertEqual(Solution().titleToNumber(string), ans)

unittest.main()
