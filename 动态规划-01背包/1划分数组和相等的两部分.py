# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 15:26
# @Author  : xiaoqing
# @File    : 1划分数组和相等的两部分.py
# @Software: PyCharm Community Edition

# 超时
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        W = int(sum(nums) / 2)
        N = len(nums)
        dp = dp = [[0 for i in range(W+1)] for j in range(N+1)]
        for i in range(1, N+1):
            w, v = nums[i-1], nums[i-1]
            for j in range(1, W+1):
                if j >= w:
                # 状态转移方程
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
                # 当前背包装不下当前物品
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[N][W] == W:
            return True
        return False

# 变成一维数组，可以通过
class Solution2(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumx = sum(nums)
        if sumx % 2 != 0:
            return False
        W = int(sumx / 2)
        N = len(nums)
        dp = [0 for i in range(W + 1)]
        for i in range(1, N + 1):
            w, v = nums[i - 1], nums[i - 1]
            for j in range(W, 0, -1):
                if j >= w:
                    dp[j] = max(dp[j], dp[j - w] + v)

        if dp[-1] == W:
            return True
        return False

a = Solution2()
r = a.canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,97,95,99,99])
print(r)