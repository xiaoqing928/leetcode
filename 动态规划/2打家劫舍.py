# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 11:16
# @Author  : xiaoqing
# @File    : 2打家劫舍.py
# @Software: PyCharm Community Edition

'''
    写出递推公式 f(n) = max{f(n-1), f(n-2)+nums[i]}
    接着一步一步写
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        p1, p2 = 0, 0
        for i in range(l):
            cur = max(p1, p2 + nums[i])
            p2 = p1
            p1 = cur
        return p1