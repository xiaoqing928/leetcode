# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 14:41
# @Author  : xiaoqing
# @File    : 2岛的数量.py
# @Software: PyCharm Community Edition


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1) + 1
            return 0
        nums = 0
        for i in range(m):
            for j in range(n):
                num = dfs(i, j)
                if num != 0:
                    nums += 1
        return nums

a = Solution()
r = a.numIslands(
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(r)