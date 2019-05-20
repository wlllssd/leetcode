#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (33.49%)
# Likes:    150
# Dislikes: 429
# Total Accepted:    40.1K
# Total Submissions: 117.4K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 0:
            return False
        temp = []
        for i in range(1,math.floor(math.sqrt(num))+1):
            if num % i == 0 and i != num:
                temp.append(i)
                if i != 1:
                    temp.append(num//i)
        print(temp)
        return sum(temp) == num and len(temp) > 0


