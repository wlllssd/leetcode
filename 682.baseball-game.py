#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        point = []
        for each in ops:
            if each == '+':
                point.append(int(point[-1]+point[-2]))
            elif each == 'D':
                point.append(int(point[-1]*2))
            elif each == 'C':
                point.pop()
            else:
                point.append(int(each))
        return sum(point)

