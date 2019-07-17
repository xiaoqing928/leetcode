# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 12:09
# @Author  : xiaoqing
# @File    : 11最长摆动子序列.py
# @Software: PyCharm Community Edition

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return 1
        dp = [1 for i in range(l)]
        for i in range(1, l-1):
            maxx = 1
            for j in range(i):
                if (nums[i] > nums[j] and nums[i] > nums[i + 1]) or (nums[i] < nums[j] and nums[i] < nums[i + 1]):
                    maxx = max(maxx, dp[j] + 1)
            dp[i] = maxx
        n1 = dp.index(max(dp))
        if max(dp) == 1:
            for i in range(l-1):
                if nums[i] != nums[i+1]:
                    return 2
            return 1
        n2 = dp.index(max(dp) - 1)
        if nums[n1] < nums[n2] and nums[n1] < nums[-1]:
            return max(dp) + 1
        elif nums[n1] > nums[n2] and nums[n1] > nums[-1]:
            return max(dp) + 1
        else:
            return max(dp)
a = Solution()
r = a.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
print(r)