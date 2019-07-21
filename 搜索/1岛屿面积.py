# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 12:01
# @Author  : xiaoqing
# @File    : 1岛屿面积.py
# @Software: PyCharm Community Edition


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) + 1
            return 0
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxarea = max(maxarea, area)
        return maxarea