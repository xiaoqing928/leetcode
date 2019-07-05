# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 19:03
# @Author  : xiaoqing
# @File    : 前K个出现频率最高的数.py
# @Software: PyCharm Community Edition

'''
    []*n 和 [[] for i in range(n)]不一样！！！'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        list1 = [[] for i in range(len(nums) + 1)]
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in list(dict1.keys()):
            v = dict1[i]
            list1[1].append(i)
            list1[v].append(i)
        cnt = 0
        res = []
        for i in range(len(nums), 0, -1):
            if cnt >= k:
                break
            if len(list1[i]) != 0:
                for j in list1[i]:
                    if cnt < k:
                        res.append(j)
                        cnt += 1
                    else:
                        break
        return res
nums = [4,1,-1,2,-1,2,3]
k = 2
a = Solution()
r = a.topKFrequent(nums, k)
print(r)


b = [[], [], []]
b[1].append(1)
b[1].append(2)
print(b)