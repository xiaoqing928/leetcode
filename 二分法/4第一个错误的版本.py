# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 10:13
# @Author  : xiaoqing
# @File    : 4第一个错误的版本.py
# @Software: PyCharm Community Edition

'''
    见leetcode
'''

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            mid = int(l + (r - l) / 2)
            if self.isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
    def isBadVersion(self):
        return True