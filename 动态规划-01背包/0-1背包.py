# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:03
# @Author  : xiaoqing
# @File    : 0-1背包.py
# @Software: PyCharm Community Edition

'''
    这个逻辑好难啊，动态规划感觉难的一匹啊！！！
    从宏观角度去观察，一个物品可以选择加入背包或者不加入背包。
    1.不加入背包：
    第 i 件物品没添加到背包，总体积不超过 j 的前 i 件物品的最大价值就是总体积不超过 j 的前 i-1 件物品的最大价值，
    dp[i][j] = dp[i-1][j]。
    2.加入背包：
    第 i 件物品添加到背包中，dp[i][j] = dp[i-1][j-w] + v

    第 i 件物品可添加也可以不添加，取决于哪种情况下最大价值更大。因此，0-1 背包的状态转移方程为：
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
'''

# 解法1 复杂度有点高
def knapsack(W, N, weights, values):
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    #一次遍历i个物品
    for i in range(1, N+1):
        # 第i个物品的重量和价值
        w, v = weights[i-1], values[i-1]
        # 依次选取所有重量
        for j in range(1, W+1):
            # 当前背包可以装下当前物品
            if j >= w:
                # 状态转移方程
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            # 当前背包装不下当前物品
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[N][W]

# 解法2 一维数组
def knapsack2(W, N, weights, values):
    dp = [0 for i in range(W + 1)]
    for i in range(1, N+1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(W, 0, -1):
            if j >= w:
                dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

weights = [1, 1, 2, 2]
values = [1, 2, 4, 5]
knapsack2(4, 4, weights, values)