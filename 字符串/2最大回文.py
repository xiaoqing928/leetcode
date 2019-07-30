# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 11:19
# @Author  : xiaoqing
# @File    : 2最大回文.py
# @Software: PyCharm Community Edition

'''
    感觉这种题没有写的价值
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        v = [dict1[i] for i in dict1.keys()]
        res = 0
        bol = 0
        for i in v:
            if i % 2 == 0:
                res += i
            else:
                res += (i - 1)
                bol = 1
        if bol == 1:
            return res + 1
        return res