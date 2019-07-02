# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 9:57
# @Author  : xiaoqing
# @File    : 3有序数组的 Single Element.py
# @Software: PyCharm Community Edition

'''
题目描述：一个有序数组只有一个数不出现两次，找出这个数。
'''
def singleNonDuplicate(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = int(l + (r-l) / 2)
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid+1]:
            l = mid + 2
        else:
            r = mid
    return nums[l]