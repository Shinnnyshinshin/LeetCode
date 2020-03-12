#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Dictionary with characters from first string. If we find a character in second string that does not exist in dictionary, return false
We add the list, and decrement. If the count reaches 0, then we remove. 
O(n)
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def myisAnagram(string1, string2):
    # simple base case
    if string1 is None or string2 is None:
        return False
    hash_for_string1 = {}
    # loop through and count the letters
    for letter in string1:
        if letter in hash_for_string1.keys():
            hash_for_string1[letter] += 1
        else:
            hash_for_string1[letter] = 1

    for letter in string2:
        # if we ever find a new letter, then we remove
        if letter not in hash_for_string1.keys():
            return False
        else:
            hash_for_string1[letter] -= 1
            if hash_for_string1[letter] is 0:
                del hash_for_string1[letter]
    if not hash_for_string1:
        return True
    else:
        return False
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def isAnagram(self, s, t):
        return myisAnagram(s,t)



#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        string1 = "anagram"
        string2 = "nagaram"
        self.assertTrue(Solution().isAnagram(string1, string2))
    def test_2(self):
        string1 = "rat"
        string2 = "car"
        self.assertFalse(Solution().isAnagram(string1, string2))

unittest.main()
