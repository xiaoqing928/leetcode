# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 16:19
# @Author  : xiaoqing
# @File    : 7.删除一个数最长子序列.py
# @Software: PyCharm Community Edition

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def cmp(x):
            return -len(x)
        d.sort(key = cmp)
        listr = []
        maxlen = 0
        for i in d:
            r = self.findWord(s, i)
            if r == True and len(i) >= maxlen:
                listr.append(i)
                maxlen = len(i)
        l = len(listr)
        if l == 0:
            return ''
        def cmp1(x):
            return str(x)
        listr.sort(key = cmp1)
        return listr[0]