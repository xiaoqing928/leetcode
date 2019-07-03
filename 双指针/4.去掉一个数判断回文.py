# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 15:13
# @Author  : xiaoqing
# @File    : 4.去掉一个数判断回文.py
# @Software: PyCharm Community Edition

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalind(s[l + 1: r+1]) or self.isPalind(s[l: r])
            else:
                l += 1
                r -= 1
        return True

    def isPalind(self, s):
        l, r = 0, len(s) - 1
        cnt = 0
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
a = Solution()
s1 = 'deeee'
r = a.validPalindrome(s1)
print(r)