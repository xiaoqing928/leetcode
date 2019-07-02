# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 21:14
# @Author  : xiaoqing
# @File    : 1求开方.py
# @Software: PyCharm Community Editio

n = 9.0
l = 0.0
def sqrt(n):
    m = n
    l = 0.0
    while l <= n:
        mid = (l + n) / 2
        if mid ** 2 == m:
            return mid
        elif mid ** 2 > m:
            n = mid
        else:
            l = mid
    return -1
r = sqrt(n)
print(r)