#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.16%)
# Total Accepted:    199.9K
# Total Submissions: 701.8K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        if n == 1 and nums[0] == 1:
            return 2
        nums.append(0)
        i = 0
        while i < n:
            if nums[i] >= 0 and nums[i] <= n and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                i -= 1
            i += 1
        print(nums)
        for i in range(n+1):
            if i != nums[i] and i > 0:
                return i
        return n+1
