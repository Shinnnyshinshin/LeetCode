#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

When it comes to canonical systems, like the US, a greedy approach will work. I'll first implement this, and we will examine the speed gain we have  

Algorithm works like the following : 

* we first sort the coins by decreasing value, meaning we subtract the biggest coins first. 
* if subtracting the current coin makes the amount go to less than 0, then we move onto the next biggest coin. 
* we continue until the amount goes to zero, and return the number of counts we have "used" so far. 


"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------
def my_coinChange_Greedy(coins, amount):
    amount_of_coins = 0
    list.sort(coins, reverse=True)
    for coin in coins:
        while amount - coin >= 0:
            amount -= coin
            amount_of_coins += 1
    return(amount_of_coins)
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def coinChange(self, coins, amount):
        return my_coinChange_Greedy(coins, amount)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    def test_100(self):
        us_denom = [1, 5, 10, 25]
        self.assertEqual(Solution().coinChange(us_denom, 100), 4)

    def test_25(self):
        us_denom = [1, 5, 10, 25]
        self.assertEqual(Solution().coinChange(us_denom, 25), 1)

    def test_24(self):
        us_denom = [1, 5, 10, 25]
        self.assertEqual(Solution().coinChange(us_denom, 24), 6)

unittest.main()
