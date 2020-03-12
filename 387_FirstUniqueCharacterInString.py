#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
    Finding repeating characters can be as easy to find if you store it in a dictionary, the key being the character and the val being the number of times it occors
    The second loop will go through and find the index in which the first non-repeating character is, and break and return
    If not then it'll return the -1 value
    Time complexity is : 2 loops O(2n) which is still O(n)
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def myfirstUniqChar(s):   
    ind_of_non_repeating_char = -1
    dict_of_chars_and_occurances = {}
    
    # first loop to add the occurances to dictionary
    for i in range(len(s)):
        current_char = s[i]
        if current_char in dict_of_chars_and_occurances.keys():
            current_count = dict_of_chars_and_occurances[current_char]
            dict_of_chars_and_occurances[current_char] = current_count + 1
        else:
            dict_of_chars_and_occurances[current_char] = 1
    
    for i in range(len(s)):
        current_char = s[i]
        if dict_of_chars_and_occurances[current_char] is 1:
            ind_of_non_repeating_char = i
            break
    return ind_of_non_repeating_char


    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def firstUniqChar(self, s):
        return myfirstUniqChar(s)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        string = "leetcode"
        ans = 0
        self.assertEqual(Solution().firstUniqChar(string), ans)

    def test_2(self):
        string = "loveleetcode"
        ans = 2
        self.assertEqual(Solution().firstUniqChar(string), ans)

unittest.main()
