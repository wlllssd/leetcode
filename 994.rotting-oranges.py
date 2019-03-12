#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.66%)
# Total Accepted:    4.1K
# Total Submissions: 8.7K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
# 
#
class Solution:
    def valid(self,i,j,row,col):
        pos = [[i,j],[i-1,j],[i+1,j],[i,j+1],[i,j-1]]
        if i-1 < 0:
            pos.remove([i-1,j])
        if j-1 < 0:
            pos.remove([i,j-1])
        if i+1 >= row:
            pos.remove([i+1,j])
        if j+1 >= col:
            pos.remove([i,j+1])
        return pos
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        # fresh_count = 0
        # rotten_count = 0
        # for each in grid:
        #     for ele in each:
        #         if ele == 1:
        #             fresh_count += 1
        #         if ele == 2:
        #             rotten_count += 1
        # total_count = fresh_count + rotten_count
        res = 0
        row = len(grid)
        col = len(grid[0])
        while True:
            change = False
            temp = copy.deepcopy(grid)
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        pos = self.valid(i,j,row,col)
                        for ele in pos:
                            if grid[ele[0]][ele[1]] == 1:
                                temp[ele[0]][ele[1]] = 2
                                change = True
            if change == False:
                break
            res += 1
            grid = temp
        for each in grid:
            for ele in each:
                if ele == 1:
                    return -1
        return res
