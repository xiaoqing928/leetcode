# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:12
# @Author  : xiaoqing
# @File    : 2最大公约数.py
# @Software: PyCharm Community Edition

def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a % b)