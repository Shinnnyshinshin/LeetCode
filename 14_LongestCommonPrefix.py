#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    * There are a number of solutions that can be implemented and I'm going to do my favorit one so far

    - Horizontal Scanning : 
        - you would take the first string and match it with the second one, taking the common prefix (if it exists)
        - and moving over to the next string and the next one, until you get to the end. 
        - if the prefix ever goes to len(x) = 0 then a prefix doesn't exist
        
        - Why don't I like this as much?:
            - if you have a really short string at the end, then you wont know until you get there
            - [ aaaaaaaaa, aaaaaaaa, a ]
    
    - Vertical Scanning (my favorite) :
        - you would check the first character for every string in the list
        - the worst case would still be the same o(n), since you would have to check every character in every string in the list, but you would catch the scenario with a short string at the end quicker. 
        - the worst case in this case would be a list of identical strings. 

    * The most complex but "fanciest" way would be to use Trie, which is basically a prefix-tree
    
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_longestCommonPrefix(strs):
    if strs is None or len(strs) is 0:
        return ""
    # getting the length of first string
    first_string = strs[0]
    for char_index in range(len(first_string)):
        current_char = first_string[char_index]
        for str_index in range(1,len(strs)):
            current_string = strs[str_index]
            if char_index == len(strs[str_index]) or strs[str_index][char_index] is not current_char:
                return first_string[0:char_index]
    return first_string


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return my_longestCommonPrefix(strs)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        input = ["flower", "flow", "flight"]
        prefix = "fl"
        self.assertEqual(Solution().longestCommonPrefix(input), prefix)
    def test_2(self):
        input = ["dog", "racecar", "car"]
        prefix = ""
        self.assertEqual(Solution().longestCommonPrefix(input), prefix)

unittest.main()
