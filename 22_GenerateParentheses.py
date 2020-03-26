#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]



"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
* One approach would be to see if we can do permutations with constraints.

What are the constraints? 
1. we can't do a ')' if we dont already have an '('
2. we can't do more ')' than '('
3. we can't have more '(' than n, which is the number of 


A great example can be found at the following website : 
https://sahandsaba.com/interview-question-generating-all-balanced-parentheses.html

It also uses something called a 'yield' function, which returns a generator. 
So what does

https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do



"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def my_generateParenthesis(n):
    table = [['']]
    for j in range(1, n+1):
        result = []
        for i in range(j):
            for x in table[i]:
                for y in table[j - i - 1]:
                    result.append('(' + x + ')' + y)
        table.append(result)
    return table[n]        

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return my_generateParenthesis(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_(self):
        string = "1"
        ans = 1
        self.assertEqual(int(string), ans)
        
unittest.main()
