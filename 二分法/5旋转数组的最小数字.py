# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 10:22
# @Author  : xiaoqing
# @File    : 5旋转数组的最小数字.py
# @Software: PyCharm Community Edition

def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l < r:
        mid = int(l + (r - l) / 2)
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]