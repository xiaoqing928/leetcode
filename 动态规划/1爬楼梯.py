# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 21:32
# @Author  : xiaoqing
# @File    : 1爬楼梯.py
# @Software: PyCharm Community Edition
'''
    动态规划，写出递推公式，f(n) = f(n-1) + f(n-2),接着一步一步写
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        p1, p2 = 1, 2
        for i in range(3, n+1):
            cur = p1 + p2
            p1, p2 = p2, cur
        return p2


class Solution1(object):
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

class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, 2, 3]
        if n <= 3:
            return arr[n-1]
        while n > 3:
            arr[0], arr[1] = arr[1], arr[2]
            arr[2] = arr[0] + arr[1]
            n -= 1
        return arr[2]