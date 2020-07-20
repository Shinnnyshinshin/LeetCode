#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""

The two pieces of information that we have : 
    1. the array length gives information about the range of numbers that we should be having? 
    2. if we find the number in the array, then it is not missing
    3. 

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

                

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_(self):
        string = "1"
        ans = 1
        self.assertEqual(int(string), ans)
        self.assertTrue(ans == 1)
        self.assertFalse(ans == 2)
        
unittest.main()
