#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
# 
#-------------------------------------------------------------------------------
#    LeetCode prompt   
#-------------------------------------------------------------------------------

"""
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
# # 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
The simplest approach is to use the Sieve of Eratosthenes, who lived about 2000 years ago. 
- The sieve takes O(n log log n) additions, along with O(n) bits of storage. 
1. we only have to look up until n**0.5, because everything else is a combination of other prime factors. 
2. we are basically going through all the prime numbers staring from 2 to n**0.5 and eliminating all multiples of the prime number (in the case of 2.. we would set 2, 4, 6, 8, 10 .. n**0.5 to false)
 
Let's talk about all the wonderful edge cases here :

1. Indices problem. Python indices start at 0, but the equations requires the indices to start at 0. So we make the prime_yes_or_no list 1 index longer than what we need, and trim at the end (with the [1:])
2. Remember we are only considering values < n. For instance if we input 2 (a prime number), then we want the function to return 0. This is accomplished by the -1 at the end. 

"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

def myCountPrimes(n):
    if n is 0:
        return 0
    prime_yes_or_no = [True for i in range(n+1)] # we are trying to use indices that match the number values
    prime_yes_or_no[1] = False # 1 is not prime
    prime_yes_or_no[0] = False # we are throwing away 0
    # we dont't have to go further than n**(1/2)
    max_ind = int(n**(0.5)) + 1 # the +1 is because we are using actual values instead of indices
    for i in range(2, max_ind):
        #print(i)
        if prime_yes_or_no[i] is True:
            # loop for turning all the factors into false
            factorval = 0
            j = i**2
            while j <= n:
                prime_yes_or_no[j] = False
                factorval += 1
                j = i**2 + (i * factorval)
                # this accomplishes :for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do

    prime_yes_or_no = prime_yes_or_no[1:-1] # we were one index off in the beginning, and we want all factors < n. 
    return(sum(prime_yes_or_no))     


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#----------------
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (myCountPrimes(n))     


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_10(self):
        self.assertEqual(Solution().countPrimes(10), 4)

unittest.main()
