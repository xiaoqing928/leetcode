# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 11:28
# @Author  : xiaoqing
# @File    : 最长harmonious数.py
# @Software: PyCharm Community Edition

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        longest = 0
        for i in dict1.keys():
            if (i + 1) in dict1:
                longest = max(longest, dict1[i] + dict1[i+1])
        return longest