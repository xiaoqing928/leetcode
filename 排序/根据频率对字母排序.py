# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 20:43
# @Author  : xiaoqing
# @File    : 根据频率对字母排序.py
# @Software: PyCharm Community Edition

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = {}
        list1 = [[] for i in range(len(s)+1)]
        res = ''
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in dict1.keys():
            v = dict1[i]
            list1[v].append(i)
        for i in range(len(list1)-1, 0, -1):
            if len(list1[i]) == 0:
                continue
            else:
                for j in list1[i]:
                    for n in range(i):
                        res += j
        return res

a = Solution()
r = a.frequencySort('aabbb')
print(r)