#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
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
    ind = -1
    if len(haystack) < len(needle):
        return ind
    if len(needle) is 0:
        return 0
    haystack_ind = 0
    first_needle_char = needle[0]
    # loop through all the haystack 
    while haystack_ind < len(haystack):
        haystack_char = haystack[haystack_ind]
        if first_needle_char is haystack_char:
            haystack_match_ind = haystack_ind
            # start matching
            for needle_match_ind in range(len(needle)):
                haystack_char = haystack[haystack_match_ind]
                needle_char = needle[needle_match_ind]
                haystack_match_ind += 1
                if needle_char != haystack_char:
                    break
            if needle_match_ind is len(needle):
                ind = haystack_match_ind  # set the thing to return
                return ind
        haystack_ind += 1
    return ind
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

    # def test_1(self):
    #     haystack = "hello"
    #     needle = "ll"
    #     ans = 2
    #     self.assertEqual(Solution().strStr(haystack, needle), ans)

    # def test_2(self):
    #     haystack = "aaaaaaa"
    #     needle = "bba"
    #     ans = -1
    #     self.assertEqual(Solution().strStr(haystack, needle), ans)

    def test_3(self):
        haystack = "mississippi"
        needle = "issip"
        ans = 4
        self.assertEqual(Solution().strStr(haystack, needle), ans)





unittest.main()
