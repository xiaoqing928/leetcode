# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 10:36
# @Author  : xiaoqing
# @File    : 6查找区间.py
# @Software: PyCharm Community Edition

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(nums) - 1
    while l < r:
        mid = int(l + (r - l) / 2)
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    left, right = l, l
    if nums[l] != target:
        return [-1, -1]
    else:
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
    return [left, right]