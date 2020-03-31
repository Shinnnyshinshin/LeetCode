#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------
"""
So this problem is made a little bit more interesting because you are sorting the digits into one array, rather than into a new one
can I 
* sorting into a new array is trivial
* but into one were you have to push one by one, then it's a different story

Possibility 1: 
    * push everything to the end, and make it 'seem' like you are adding to a new array
    * but that isn't going to be good enough

Possibility 2: 
    * you can swap
    * so you have to put it back, but you dont know if it's a major jumpr or not 

    nums 1 = [1, 10]
    nums 2 = [2, 3, 4]

    * you couldn't just swap and assume that everything is going to be ok 

Possibility 3: 
    * can i start from the back? 
    * 3 pointers
        * a = starting from end of nums1 
        * b = starting from m and traversing nums1
        * c = starting from n and traversing nums2
"""


#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_merge(nums1, m, nums2, n):
    # set up 3 pointer
    end_pt = len(nums1)-1
    nums1_pt = m - 1 
    nums2_pt = n - 1
    # traversing down
    # let's try a while loop this time
    while nums2_pt >= 0:
        if nums1_pt < 0 or nums2[nums2_pt] >= nums1[nums1_pt]:
            nums1[end_pt] = nums2[nums2_pt]
            nums2_pt -= 1
            end_pt -= 1
        else:
            nums1[end_pt] = nums1[nums1_pt]
            nums1_pt -= 1 
            end_pt -= 1
    return nums1

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        return my_merge(nums1, m, nums2, n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
class TestSolution(unittest.TestCase):
    def test_given(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        ans = [1, 2, 2, 3, 5, 6]
        self.assertEqual(Solution().merge(nums1, m, nums2, n), ans)
    def test_submission_1(self):
        nums1 = [2, 0]
        m = 1 
        nums2 = [1]
        n = 1 
        ans = [1, 2]
        self.assertEqual(Solution().merge(nums1, m, nums2, n), ans)

unittest.main()
