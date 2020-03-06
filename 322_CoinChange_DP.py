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
This second approach is through DP. It is a very good example of a problem that contains the two "hallmarks" 
of a DP problem, namely overlapping subproblems and overlapping structure. 

* the overlapping substructure : 


"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------


def my_coinChange_DP(coins, num_to_search):
    # V = num to search
    
    num_coins = len(coins)
    table = [0 for i in range(num_to_search + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, num_to_search + 1):
        table[i] = sys.maxsize

    for i in range(1, num_to_search + 1):
        for j in range(num_coins):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    return table[num_to_search]


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
