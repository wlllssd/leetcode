#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.08%)
# Total Accepted:    288.4K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or (first_match and self.isMatch[s[1:],p])
        else:
            return first_match and self.isMatch(s[1:],p[1:])
