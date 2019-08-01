# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 10:28
# @Author  : xiaoqing
# @File    : 3字符串同构.py
# @Software: PyCharm Community Edition

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = len(s), len(t)
        dict1, dict2 = {}, {}
        if l1 != l2:
            return False
        for i in range(l1):
            if s[i] in dict1 and t[i] in dict2 and dict1[s[i]] != dict2[t[i]]:
                return False
            if s[i] in dict1 and t[i] not in dict2:
                return False
            if s[i] not in dict1 and t[i] in dict2:
                return False
            dict1[s[i]] = i
            dict2[t[i]] = i
        return True
a = Solution()
s, t = 'aa', 'ab'
r = a.isIsomorphic(s, t)
print(r)