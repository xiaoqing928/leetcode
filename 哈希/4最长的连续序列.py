# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 9:44
# @Author  : xiaoqing
# @File    : 4最长的连续序列.py
# @Software: PyCharm Community Edition

'''
第一步判断左右两边是否存在数，存在则加上
第二步将最长子序列两端key的value补位长度的最大值
eg:[1,2,4,3]
{1:1}
{1:2, 2:2}
{1:2, 2:2, 4:1}
{1:4, 2:2, 3:4, 4:4}
'''
def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    record = {}
    res = 0
    for n in nums:
        # 如果不存在 则为1
        if n not in record:
            record[n] = 1
            #右边有加上右边的
            if n + 1 in record:
                record[n] += record[n + 1]
            #左边有加上左边的
            if n - 1 in record:
                record[n] += record[n - 1]
            # 两端key的value设置为最长子序列
            r = n + 1
            while r in record:
                r = r + 1
            #右端的
            record[r - 1] = record[n]
            l = n - 1
            while l in record:
                l = l - 1
            #左端的
            record[l + 1] = record[n]
            res = max(res, record[n])
    return res