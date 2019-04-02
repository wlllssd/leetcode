#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.44%)
# Total Accepted:    183.2K
# Total Submissions: 685K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 0
        if not head:
            return None
        # 1
        if not head.next or k==0:
            return head
        # 2 or more
        length = 1
        pointer = head
        while pointer.next:
            length += 1
            pointer = pointer.next
        rotate = k % length
        if rotate == 0:
            return head
        slow = head
        fast = head
        for i in range(rotate):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next,fast.next,head = None,head,slow.next
        
        return head

