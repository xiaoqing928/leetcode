# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 21:05
# @Author  : xiaoqing
# @File    : 荷兰国旗排序.py
# @Software: PyCharm Community Edition

'''
    这个似乎更简单了
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = -1, len(nums)
        cur = 0
        while cur < r:
            if nums[cur] < 1:
                l += 1
                self.swap(nums, cur, l)
                cur += 1
            elif nums[cur] > 1:
                r -= 1
                self.swap(nums, cur, r)
            else:
                cur += 1
        return nums

    def swap(self, nums, m, n):
        tmp = nums[m]
        nums[m] = nums[n]
        nums[n] = tmp

