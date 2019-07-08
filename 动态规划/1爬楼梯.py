# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 21:32
# @Author  : xiaoqing
# @File    : 1爬楼梯.py
# @Software: PyCharm Community Edition

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [1, 2, 3]
        if n < 4:
            return fib[n-1]
        for i in range(3, n+1):
            fib[2] = fib[0] + fib[1]
            fib[0], fib[1] = fib[1], fib[2]
        return fib[2]