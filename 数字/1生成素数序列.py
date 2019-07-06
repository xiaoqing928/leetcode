# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 10:44
# @Author  : xiaoqing
# @File    : 1生成素数序列.py
# @Software: PyCharm Community Edition

'''
    最初全部默认为素数，找到一个素数之后，将能被素数整除的数排除掉

'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        list1 = [False for i in range(n)]
        cnt = 0
        for i in range(2, n):
            if list1[i]:
                continue
            cnt += 1
            #从 i * i 开始，因为如果 k < i，那么 k * i 在之前就已经被去除过了
            for j in range(i*i, n, i):
                list1[j] = True
        return cnt