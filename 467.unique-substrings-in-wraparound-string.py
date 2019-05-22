#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (33.41%)
# Likes:    357
# Dislikes: 57
# Total Accepted:    18.1K
# Total Submissions: 53.4K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
# 
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
# 
# Example 1:
# 
# Input: "a"
# Output: 1
# 
# Explanation: Only the substring "a" of string "a" is in the string s.
# 
# 
# 
# Example 2:
# 
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
# 
# 
# 
# Example 3:
# 
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
# 
# 
#
from collections import defaultdict
class Solution:
    def next(self,a,b):
        if ord(b)-ord(a) == 1 or (a == 'z' and b == 'a'):
            return True
        else:
            return False

    def findSubstringInWraproundString(self, p: str) -> int:
        i = 0
        res = defaultdict(int)
        while i < len(p):
            start = i
            while i < len(p) - 1 and self.next(p[i],p[i+1]):
                i += 1
            end = i
            for j,k in enumerate(range(start,end+1)):
                ele = p[k]
                res[ele] = max(res[ele],end-start+1-j)
            i += 1
        count = 0
        for i in res:
            count += res[i]
        return count

