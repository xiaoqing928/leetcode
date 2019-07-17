# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 11:31
# @Author  : xiaoqing
# @File    : 9最长递增字串.py
# @Software: PyCharm Community Edition

'''
    发现严格的套路化
    动态规划：建立dp数组，根据条件往里填数
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        # 这里也可以不用numpy
        import numpy as np
        dp = np.array([0] * l)
        #外层循环 每次都和前边的比
        for i in range(l):
            maxx = 1
            # 内层循环
            for j in range(i):
                # 如果满足条件
                if nums[i] > nums[j]:
                    # 在maxx和前边保存的信息中选取更大的
                    maxx = max(maxx, dp[j] + 1)
            dp[i] = maxx
        return np.max(dp)