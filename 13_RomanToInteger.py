#-------------------------------------------------------------------------------
#    
#-------------------------------------------------------------------------------
# By Will Shin
#
#-------------------------------------------------------------------------------
#    LeetCode prompt
#-------------------------------------------------------------------------------

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_romanToInt(roman):
    # set up the variable
    letter_to_val = {}
    letter_to_val['I'] = 1
    letter_to_val['V'] = 5
    letter_to_val['X'] = 10
    letter_to_val['L'] = 50
    letter_to_val['C'] = 100
    letter_to_val['D'] = 500
    letter_to_val['M'] = 1000
    
    integer_sum = 0 
    roman_index = 0
    while(roman_index < len(roman)):
        try:
            current_char = roman[roman_index]
            next_char = roman[roman_index+1]
            if letter_to_val[next_char] > letter_to_val[current_char]:
                # then we have a situation where we need to add it
                num_to_add = letter_to_val[next_char] - letter_to_val[current_char]
                integer_sum += num_to_add
                roman_index += 2
            else:
                num_to_add = letter_to_val[current_char]
                integer_sum += num_to_add
                roman_index += 1
        except (KeyError, IndexError):
            num_to_add = letter_to_val[current_char]
            integer_sum += num_to_add
            roman_index += 1
    return integer_sum
 
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------


class Solution:
    def romanToInt(self, s):
        return my_romanToInt(s)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_3(self):
        string = "III"
        ans = 3
        self.assertEqual(Solution().romanToInt(string), ans)
        
    def test_4(self):
        string = "IV"
        ans = 4
        self.assertEqual(Solution().romanToInt(string), ans)

    def test_9(self):
        string = "IX"
        ans = 9
        self.assertEqual(Solution().romanToInt(string), ans)

    def test_58(self):
        string = "LVIII"
        ans = 58
        self.assertEqual(Solution().romanToInt(string), ans)

    def test_1994(self):
        string = "MCMXCIV"
        ans = 1994
        self.assertEqual(Solution().romanToInt(string), ans)

unittest.main()
