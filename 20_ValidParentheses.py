#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
# 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
    1. This seems to be a simple stack algorithm, which is a list in python 3
    2. Will use a peek at the end of hte 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def myIsValid(inputstring):
    mystack = []
    pairs_dict = {')': '(', '}' : '{', ']':'['}
    charlist= [char for char in inputstring]
    for char in charlist:
        if char in ['(', '{', '[']:
            mystack.append(char)
        else:
            if len(mystack) == 0:
                return False
            elif mystack[-1] is not pairs_dict[char]:
                return False
            else:
                mystack.pop()
    if len(mystack) == 0:
        return True
    return False              

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution(object):
    def isValid(self, s):
        return myIsValid(s)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        input = "()"
        ans = True
        self.assertEqual(Solution().isValid(input), ans)


    def test_series(self):
        input = "()[]{}"
        ans = True
        self.assertEqual(Solution().isValid(input), ans)


    def test_simple_mismatch(self):
        input = "(]"
        ans = False
        self.assertEqual(Solution().isValid(input), ans)


    def test_wrongorder(self):
        input = "([)]"
        ans = False
        self.assertEqual(Solution().isValid(input), ans)


    def test_complex_truth(self):
        input = "{[]}"
        ans = True
        self.assertEqual(Solution().isValid(input), ans)


        
unittest.main()
