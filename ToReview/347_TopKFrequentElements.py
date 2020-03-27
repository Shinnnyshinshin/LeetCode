#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
    * The simplest way would be to build a hashtable with the frequencies of each letter
    * we would loop through the list 2 times?  O(n)


    * But we can do better. We can use a Heap to make the data structure more efficient. 

    * Heap data structure is mainly used to represent a priority queue. 
    * In Python, it is available using “heapq” module. 
    * The property of this data structure in python is that each time the smallest of 
    * heap element is popped(min heap). 
    * Whenever elements are pushed or popped, heap structure in maintained. 
    * The heap[0] element also returns the smallest element each time.

    * In Python there is a method nlargest in heapq library (check here the source code) 
    * which has the same O(log(k)) time complexity 
    * and combines two last steps in one line.
"""
#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_topKFrequent(nums, k):
    
    # build the hashtable first
    """ # this is the "simple" way to build it. There is a better way through collections
    freq_dict = {}
    for num in nums:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            count = freq_dict[num]
            freq_dict[num] = count + 1
    """
    # better way to do this
    freq_dict = collections.Counter(nums)
    return heapq.nlargest(k, freq_dict.keys(), key=freq_dict.get)    
    # there is a better way to do this # d, h = [(freq, num) for num, freq in Counter(nums).items()], []
    #
    # build a heap


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return my_topKFrequent(nums, k)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
import heapq
import collections
class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual(Solution().topKFrequent(nums, k), [1, 2])
    
    def test_2(self):
        nums = [1]
        k = 1
        self.assertEqual(Solution().topKFrequent(nums, k), [1])

unittest.main()
