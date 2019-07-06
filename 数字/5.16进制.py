# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:51
# @Author  : xiaoqing
# @File    : 5.16进制.py
# @Software: PyCharm Community Edition

def way1(self, num):
    hex_l = list(map(str, range(0, 10))) + ['a', 'b', 'c', 'd', 'e', 'f']
    ans = ''
    if num < 0:
        num += 2 ** 32  # 补码
    while num >= 16:
        num, mod = divmod(num, 16)
        ans += hex_l[mod]
    ans += hex_l[num]
    return ans[::-1]