# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 10:55
# @Author  : xiaoqing
# @File    : 4整数是否是回文.py
# @Software: PyCharm Community Edition

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x <= 9:
            return True
        if x < 0:
            return False
        right = 0
        while right < x:
            right = right * 10 + x % 10
            x = int(x / 10)
        return right == x or x == int(right /10)

a = Solution()
r = a.isPalindrome(121)
print(r)