# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 11:37
# @Author  : xiaoqing
# @File    : 10最大长度的链.py
# @Software: PyCharm Community Edition

'''
    动态规划：有很高的套路
    排序sort（key）lambda函数
    列表表达式生成dp数组
'''

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l = len(pairs)
        pairs.sort()
        if l == 0:
            return 0
        # 使用列表生成式产生数组
        dp = [1 for i in range(l)]
        for i in range(l):
            maxx = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    maxx = max(maxx, dp[j] + 1)
            dp[i] = maxx
        return max(dp)

a = [[2,3], [1,2], [1,4]]
# r = Solution()
# r.findLongestChain(a)
a.sort(key=lambda x: x[1])
print(a)