# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 15:10
# @Author  : xiaoqing
# @File    : 3朋友圈.py
# @Software: PyCharm Community Edition


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        isVisited = [0 for i in range(m)]
        def dfs(i, isvisited):
            isvisited[i] = 1
            for j in range(m):
                if M[i][j] == 1 and isvisited[j] == 0:
                    dfs(j, isvisited)
        nums = 0
        for i in range(m):
            if isVisited[i] == 0:
                dfs(i, isVisited)
                nums += 1
        return nums
arr = [[1,0,0],[0,1,0],[0,0,1]]
a = Solution()
r = a.findCircleNum(arr)
print(r)