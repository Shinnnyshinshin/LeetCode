#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""

    What are some ways that we can do this?

    we can calculate the min-max, the number of peaks, or we can take little steps at a time

    since we have an unlimited number of transactions, everytime something goes up, then we can make a transaction

    so our condition becomes very simple: 

    If our current value is more than the previous value, then we add the difference to the sum/total profit. 
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def my_maxProfit(prices):
    sum_to_return = 0
    prev_val = prices[0]
    for index in range(1,len(prices)):
        current_val = prices[index]
        if prev_val < current_val:
            sum_to_return += current_val - prev_val
        prev_val = current_val

    return(sum_to_return)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices):
        return my_maxProfit(prices)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        input = [7, 1, 5, 3, 6, 4]
        ans = 7
        self.assertEqual(Solution().maxProfit(input), ans)

    def test_2(self):
        input = [1, 2, 3, 4, 5]
        ans = 4 
        self.assertEqual(Solution().maxProfit(input), ans)

    def test_3(self):
        input = [7, 6, 4, 3, 1]
        ans = 0 
        self.assertEqual(Solution().maxProfit(input), ans)

unittest.main()
