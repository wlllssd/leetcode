#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (57.45%)
# Total Accepted:    60.6K
# Total Submissions: 105.5K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# Output: [1, 3, 9]
#
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
    def largestValues(self, root: TreeNode) -> List[int]:
        level = [root]
        res = []
        while any(level):
            largest = -2147483648
            temp = []
            for i in range(len(level)):
                if level[i].left:
                    temp.append(level[i].left)
                if level[i].right:
                    temp.append(level[i].right)
                largest = max(largest, level[i].val)
            level.clear()
            level = temp
            res.append(largest)
        return res
