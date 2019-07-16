# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 15:03
# @Author  : xiaoqing
# @File    : 7数组中等差递增子区间的个数.py
# @Software: PyCharm Community Edition

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        import numpy as np
        dp = np.array([0] * l)
        for i in range(2, l):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)