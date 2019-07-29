# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 10:42
# @Author  : xiaoqing
# @File    : 1l两数之和.py
# @Software: PyCharm Community Edition

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict1:
                return [dict1[target - nums[i]], i]
            else:
                dict1[nums[i]] = i
        return None

a = Solution()
r = a.twoSum([2,7,11,15], 9)
print(r)