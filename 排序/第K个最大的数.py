# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 11:45
# @Author  : xiaoqing
# @File    : 第K个最大的数.py
# @Software: PyCharm Community Edition

'''
    使用小根堆
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)