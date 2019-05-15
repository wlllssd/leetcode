#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.33%)
# Likes:    952
# Dislikes: 217
# Total Accepted:    57.9K
# Total Submissions: 172K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges
# between them.
#
#
#
# Example 1:
#
# Input:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    longest = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        

        def traverse(root):

            if not root:
                return 0
            left_len, right_len = traverse(root.left), traverse(root.right)
            if root.left and root.val == root.left.val:
                left = left_len+1
            else:
                left = 0

            if root.right and root.val == root.right.val:
                right = right_len+1
            else:
                right = 0
            
            self.longest = max(self.longest,left+right)
            return max(left,right)
        traverse(root)
        return self.longest
            
