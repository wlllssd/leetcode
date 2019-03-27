#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (30.33%)
# Total Accepted:    259.5K
# Total Submissions: 848K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution:
    def dfs(self,board,i,j,word,index):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if word[index] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        result = self.dfs(board,i+1,j,word,index+1) or self.dfs(board,i-1,j,word,index+1) or self.dfs(board,i,j+1,word,index+1) or self.dfs(board,i,j-1,word,index+1)
        board[i][j] = temp
        return result

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word,0):
                    return True
        return False

