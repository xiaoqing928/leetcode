# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 11:39
# @Author  : xiaoqing
# @File    : 3环形打家劫舍.py
# @Software: PyCharm Community Edition

'''
    思路：删掉第一个点寻找一轮，再删掉最后一个点寻找一轮，比较两次结果中的最大值。
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        p1, p2, p3, p4 = 0, 0, 0, 0
        for i in range(l):
            if i < l-1:
                cur1 = max(p1, p2 + nums[i])
                p2 = p1
                p1 = cur1
            if i > 0:
                cur2 = max(p3, p4 + nums[i])
                p4 = p3
                p3 = cur2
        return max(p1, p3)