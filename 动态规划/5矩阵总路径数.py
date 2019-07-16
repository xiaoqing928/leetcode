# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 15:00
# @Author  : xiaoqing
# @File    : 5矩阵总路径数.py
# @Software: PyCharm Community Edition

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import numpy as np
        dp = np.array([0] * n)
        for j in range(n):
            dp[j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return int(dp[-1])