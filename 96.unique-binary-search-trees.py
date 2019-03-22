#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (45.00%)
# Total Accepted:    188.4K
# Total Submissions: 415.4K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
class Solution:
    def numTrees(self, n: int) -> int:
        l = [0] * (n+1)
        if n < 2:
            return 1
        l[0] = 1
        l[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                left = j
                right = i-j-1
                l[i] += l[left] * l[right]
        return l[n]
