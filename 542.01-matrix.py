#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (34.99%)
# Total Accepted:    39.4K
# Total Submissions: 112.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#
#


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dis = [[10000] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
        for times in range(10):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if dis[i][j] == 0:
                        continue
                    else:
                        dis[i][j] = min(dis[i+ele[0]][j+ele[1]]+1 for ele in adj if i+ele[0] >=
                                        0 and i+ele[0] < len(matrix) and j+ele[1] >= 0 and j+ele[1] < len(matrix[0]))
        return dis
