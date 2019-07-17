# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 15:39
# @Author  : xiaoqing
# @File    : 8分割整数的最大乘积.py
# @Software: PyCharm Community Edition

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        dp = np.array([0] * (n + 1))
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
