# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:08
# @Author  : xiaoqing
# @File    : 4最小矩阵和.py
# @Software: PyCharm Community Edition

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        import numpy as np
        dp = np.zeros((m, n))
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

# a = Solution()
# r = a.minPathSum(
# [[1,3,1],[1,5,1],[4,2,1]])
# print(r)

class Solution1(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        m, n = len(grid), len(grid[0])
        dp = np.array([0] * n)
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                if j == 0:
                    dp[j] += grid[i][0]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return int(dp[-1])

a = Solution1()
a.minPathSum([[1,3,1],[1,5,1],[4,2,1]])