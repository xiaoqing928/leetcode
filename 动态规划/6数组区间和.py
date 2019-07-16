# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 15:00
# @Author  : xiaoqing
# @File    : 6数组区间和.py
# @Software: PyCharm Community Edition

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        l = len(nums)
        if l == 0:
            return None
        import numpy as np
        self.dp = np.array([0] * l)
        self.dp[0] = nums[0]
        for m in range(1, l):
            self.dp[m] = self.dp[m-1] + nums[m]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.dp[j] - self.dp[i - 1]
        else:
            return self.dp[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)