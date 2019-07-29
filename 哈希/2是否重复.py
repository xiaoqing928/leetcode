# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 11:04
# @Author  : xiaoqing
# @File    : 2是否重复.py
# @Software: PyCharm Community Edition

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                return True
            else:
                dict1[nums[i]] = 1
        return False