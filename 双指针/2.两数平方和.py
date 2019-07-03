# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 16:51
# @Author  : xiaoqing
# @File    : 2.两数平方和.py
# @Software: PyCharm Community Edition

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        r = int(math.sqrt(c))
        l = 0
        while l <= r:
            if l ** 2 + r ** 2 == c:
                return True
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                r -= 1
        return False