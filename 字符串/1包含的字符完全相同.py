# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:41
# @Author  : xiaoqing
# @File    : 1包含的字符完全相同.py
# @Software: PyCharm Community Edition
'''
    比较简答，直接使用hash，判断个数是否相等就可以了
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts, dictt = {}, {}
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        for i in t:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
        l = list(dictt.keys())
        s = list(dicts.keys())
        if len(l) != len(s):
            return False
        for i in s:
            if (i not in l) or dictt[i] != dicts[i]:
                return False
        return True