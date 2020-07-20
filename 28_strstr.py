#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#  LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
* there is of course the trivial answer of if needle in haystack, but we are going to make things a little bit more complicated :)

The approach will use 

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------
def my_strStr(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution:
    def strStr(self, haystack, needle):
        return my_strStr(haystack, needle)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        haystack = "hello"
        needle = "ll"
        ans = 2
        self.assertEqual(Solution().strStr(haystack, needle), ans)

    def test_2(self):
        haystack = "aaaaaaa"
        needle = "bba"
        ans = -1
        self.assertEqual(Solution().strStr(haystack, needle), ans)

    def test_3(self):
        haystack = "mississippi"
        needle = "issip"
        ans = 4
        self.assertEqual(Solution().strStr(haystack, needle), ans)

    def test_4(self):
        haystack = "mississippi"
        needle = "issipi"
        ans = -1
        self.assertEqual(Solution().strStr(haystack, needle), ans)





unittest.main()
