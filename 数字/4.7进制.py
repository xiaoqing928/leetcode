# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:26
# @Author  : xiaoqing
# @File    : 4.7进制.py
# @Software: PyCharm Community Edition

'''
    掌握到如何计算的就ok  每次除以7，得到余数，知道商为0停止，最后将余数倒序输出
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1 = []
        if num == 0:
            return '0'
        if num > 0:
            a = ''
        else:
            a = '-'
        num = abs(num)
        while num > 0:
            list1.insert(0, num % 7)
            num = int(num / 7)
        for i in list1:
            a += str(i)
        return a
a = Solution()
r = a.convertToBase7(-7)
print(r)