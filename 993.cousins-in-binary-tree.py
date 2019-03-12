#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (54.30%)
# Total Accepted:    4.9K
# Total Submissions: 9K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
# 
# 
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
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        stack = []
        stack.append(root)
        while len(stack) > 0:
            temp = []
            appear = 0
            parent1 = 0
            parent2 = 0
            while not len(stack) == 0:
                ele = stack.pop()
                if ele.left:
                    temp.append(ele.left)
                    if x == ele.left.val or y == ele.left.val:
                        appear += 1
                        parent1 = ele
                if ele.right:
                    temp.append(ele.right)
                    if x == ele.right.val or y == ele.right.val:
                        appear += 1
                        parent2 = ele
            stack = temp

            if appear == 2:
                if parent1 is parent2:
                    print("This")
                    return False
                else:
                    return True
            if appear == 1:
                return False
            
        return False
