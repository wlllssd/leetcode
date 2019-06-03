#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (62.11%)
# Likes:    375
# Dislikes: 22
# Total Accepted:    43.5K
# Total Submissions: 68.8K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# 
# Note:
# 
# 
# Both of the given trees will have between 1 and 100 nodes.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isleaf(self,root):
        if not (root.left or root.right):
            return True
        else:
            return False

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not (root1 and root2):
            return False
        if self.isleaf(root1) and self.isleaf(root2):
            if root1.val == root2.val:
                return True
            else:
                return False
        elif not self.isleaf(root1) and not self.isleaf(root2):
            return self.leafSimilar(root1.left,root2.left) and self.leafSimilar(root1.right,root2.right)
        else:
            return False


