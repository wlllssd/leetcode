#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (52.66%)
# Likes:    1598
# Dislikes: 154
# Total Accepted:    150.6K
# Total Submissions: 282.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.append(0)
        res = []
        for i in range(len(nums)):
            while nums[nums[i]] != nums[i]:
                nums[nums[i]],nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i and i != 0:
                res.append(i)
        return res

