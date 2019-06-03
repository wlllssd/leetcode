#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.62%)
# Likes:    1623
# Dislikes: 108
# Total Accepted:    336.6K
# Total Submissions: 720K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
#
#
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for word in sorted(strs):
            key = tuple(sorted(word))
            res[key] = res.get(key, []) + [word]
        return res.values()
