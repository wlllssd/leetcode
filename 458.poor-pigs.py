#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#
# https://leetcode.com/problems/poor-pigs/description/
#
# algorithms
# Easy (44.89%)
# Total Accepted:    14.8K
# Total Submissions: 32.9K
# Testcase Example:  '1000\n15\n60'
#
# There are 1000 buckets, one and only one of them contains poison, the rest
# are filled with water. They all look the same. If a pig drinks that poison it
# will die within 15 minutes. What is the minimum amount of pigs you need to
# figure out which bucket contains the poison within one hour.
# 
# Answer this question, and write an algorithm for the follow-up general case.
# 
# Follow-up: 
# 
# If there are n buckets and a pig drinking poison will die within m minutes,
# how many pigs (x) you need to figure out the "poison" bucket within p
# minutes? There is exact one bucket with poison.
# 
#
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest // minutesToDie
        i = 0
        while True:
            if (n+1) ** i >= buckets:
                return i
            i += 1

