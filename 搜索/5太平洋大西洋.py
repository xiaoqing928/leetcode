# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 16:32
# @Author  : xiaoqing
# @File    : 5太平洋大西洋.py
# @Software: PyCharm Community Edition

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        def dfs(i, j, isarrive):
            if i == 0 or j == 0:
                # 可以到太平洋
                isarrive[0] = 1
            if i == m-1 or j == n-1:
                # 可以到大西洋
                isarrive[1] = 1
            if i > 0 and matrix[i][j] >= matrix[i-1][j]:
                return dfs(i-1, j, isarrive)
            if i < m - 1 and matrix[i][j] >= matrix[i+1][j]:
                return dfs(i+1, j, isarrive)
            if j > 0 and matrix[i][j] >= matrix[i][j-1]:
                return dfs(i, j-1, isarrive)
            if j < n - 1 and matrix[i][j] >= matrix[i][j+1]:
                return dfs(i, j+1, isarrive)
            return 0
        result = []
        for i in range(m):
            for j in range(n):
                isarrive = [0, 0]
                num = dfs(i, j, isarrive)
                if num == 2:
                    result.append([i, j])
        return result


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []

        r, c = len(matrix), len(matrix[0])
        if r == 1 and c == 1: return [[0, 0]]
        self.dp = [[False for _ in range(c)] for _ in range(r)]

        res = []

        for i in range(r):
            for j in range(c):
                self.pac, self.alt = False, False
                self.dfs(matrix, i, j, [])
                if self.pac and self.alt:
                    res.append([i, j])
                    self.dp[i][j] = True

        return res

    def dfs(self, board, i, j, rec):
        if self.dp[i][j]:
            self.pac, self.alt = True, True
            return
        if self.pac and self.alt: return
        if not (0 <= i <= len(board)) or not (0 <= j <= len(board[0])) or [i, j] in rec:
            return
        if i == 0 or j == 0:
            self.pac = True
        if i == len(board) - 1 or j == len(board[0]) - 1:
            self.alt = True

        rec.append([i, j])

        if i > 0 and board[i][j] >= board[i - 1][j]:
            self.dfs(board, i - 1, j, rec[:])
        if i < len(board) - 1 and board[i][j] >= board[i + 1][j]:
            self.dfs(board, i + 1, j, rec[:])
        if j > 0 and board[i][j] >= board[i][j - 1]:
            self.dfs(board, i, j - 1, rec[:])
        if j < len(board[0]) - 1 and board[i][j] >= board[i][j + 1]:
            self.dfs(board, i, j + 1, rec[:])

a = Solution()
mat = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
r = a.pacificAtlantic(mat)
print(r)