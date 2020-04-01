#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    Ok so this is clearly some sort of dynamic programming problem. 
    
    * each row gets to look one above it, except the previous one. 
    * 
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_generate(numRows):
    if numRows is 0:
        return []
    if numRows is 1:
        return [[1]]
    # initialize
    triangle = [[1]]
    # the i index goes through each row. 
    for i in range(1, numRows):
        row = [1]
        # this is each item in the current row ( which is the same as )
        for j in range(1,i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
            

    

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return my_generate(numRows)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1row(self):
        numrow = 1
        ans = [ [1] ] 
        self.assertEqual(Solution().generate(numrow), ans)

    def test_2row(self):
        numrow = 2 
        ans = [[1], [1,1]]
        self.assertEqual(Solution().generate(numrow), ans)

    def test_3row(self):
        numrow = 3 
        ans = [[1], [1,1], [1,2,1]]
        self.assertEqual(Solution().generate(numrow), ans)



unittest.main()
