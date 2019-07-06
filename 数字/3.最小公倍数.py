# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:15
# @Author  : xiaoqing
# @File    : 3.最小公倍数.py
# @Software: PyCharm Community Edition

def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a % b)
'''
    最小公倍数等于两数相乘 除以最大公约数
'''
def lcm(a, b):
    return a * b / gcd(a, b)