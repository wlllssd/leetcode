#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (45.00%)
# Likes:    235
# Dislikes: 30
# Total Accepted:    48.1K
# Total Submissions: 101.5K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# 
# Note:
# 
# 
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
# 
# 
#
class Solution:
    def bs(self, nums, target, start, end):
        n = (start + end) // 2
        if start >= end:
            return -1
        if target == nums[n]:
            return n
        elif target > nums[n]:
            return self.bs(nums,target,n+1,end)
        elif target < nums[n]:
            return self.bs(nums,target,start,n)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums,target,0,len(nums))

