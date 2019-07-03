# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 8:52
# @Author  : xiaoqing
# @File    : 1 两数之和（二）.py
# @Software: PyCharm Community Edition

'''
    双指针，一个从前往后，一个从后往前。

'''
def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1