# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 10:14
# @Author  : xiaoqing
# @File    : 加括号.py
# @Software: PyCharm Community Edition

'''
    从整体上去考虑
    左边有多少种情况，右边有多少种情况，
    左边和右边再做一个排列组合
    其实整个过程类似于归并排序
    要多思考多想！！
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        l = len(input)
        ways = []
        for i in range(l):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for m in left:
                    for n in right:
                        if c == '+':
                            ways.append(m + n)
                        if c == '-':
                            ways.append(m - n)
                        if c == '*':
                            ways.append(m * n)

        if len(ways) == 0:
            ways.append(int(input))
        return ways
a = Solution()
r = a.diffWaysToCompute('2*3-4*5')
print(r)
