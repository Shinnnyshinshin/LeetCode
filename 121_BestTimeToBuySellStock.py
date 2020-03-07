#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""

121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------
"""

A naive approach would be to examine every possible buy and sell combination. 

* A X B grid : where we have each of the buy and sell dates. We have one major constraint that we can eliminate half the grid where A <= B. 
* If we are only buying and selling once, we only have to look at max and min, as long as the max is after the min
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


def my_maxProfit(prices):
    max_profit = 0

    if len(prices) >= 2:
        max_profit = prices[1] - prices[0]  # this is the first option
        min_ind = 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - prices[min_ind], prices[i] - prices[i-1])
            if prices[i-1] < prices[min_ind]:
                min_ind = i-1

    if max_profit < 0:
        max_profit = 0
    return max_profit

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return my_maxProfit(prices)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest
import sys
class TestSolution(unittest.TestCase):
    """
    def test_first(self):
        prices = [1, 7, 2, 3, 6, 7, 6, 7]
        ans = 6
        self.assertEqual(Solution().maxProfit(prices), ans)
    def test_second(self):
        prices = [7, 1, 5, 3, 6, 4]
        ans = 5
        self.assertEqual(Solution().maxProfit(prices), ans)
    """
    def test_third(self):
        prices =[2, 1, 4]
        ans = 3
        self.assertEqual(Solution().maxProfit(prices), ans)


unittest.main()
