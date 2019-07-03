# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 15:46
# @Author  : xiaoqing
# @File    : 5.merge排序数组.py
# @Software: PyCharm Community Editio

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = 0, 0
        help_arr = []
        while l1 < m and l2 < n:
            if nums1[l1] <= nums2[l2]:
                help_arr.append(nums1[l1])
                l1 += 1
            else:
                help_arr.append(nums2[l2])
                l2 += 1
        if l1 < m:
            for i in nums1[l1:m]:
                help_arr.append(i)
        else:
            for i in nums2[l2:n]:
                help_arr.append(i)
        return help_arr

a = Solution()
r = a.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
print(r)