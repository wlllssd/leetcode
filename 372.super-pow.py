#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.45%)
# Total Accepted:    26.8K
# Total Submissions: 75.4K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
# 
# Example 1:
# 
# 
# 
# Input: a = 2, b = [3]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# 
# 
#
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for ele in b:
            res = pow(res,10,1337) * pow(a,ele,1337) % 1337
        return res

