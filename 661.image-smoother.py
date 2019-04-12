#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (47.86%)
# Total Accepted:    32.6K
# Total Submissions: 67.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
#
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
#
#
# Note:
#
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
#
#
import copy
import math


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        adj = [[0, 0], [-1, 0], [-1, 1], [-1, -1],
               [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
        res = copy.deepcopy(M)
        row, col = len(M), len(M[0])
        angle = [[0, 0], [0, col-1], [row-1, 0], [row-1, col-1]]
        for i in range(row):
            for j in range(col):
                total = 9
                value = 0
                for ele in adj:
                    if i+ele[0] < 0 or i+ele[0] >= row or j+ele[1] < 0 or j+ele[1] >= col:
                        total -= 1
                        continue
                    value += M[i+ele[0]][j+ele[1]]
                res[i][j] = math.floor(value/total)
        return res
