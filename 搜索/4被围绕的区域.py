# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 16:10
# @Author  : xiaoqing
# @File    : 4被围绕的区域.py
# @Software: PyCharm Community Edition

'''
    哈哈哈 笑出猪叫 啦啦啦 感觉掌握了诀窍啊
    不同的问题 不同的分析  但是跑不出dfs、bfs的范畴
    看如何使用dfs的策略，不论是寻找最大的面积、小岛的数量还是填充数字
    无非就是在dfs中稍加变化

    对于朋友圈的问题，需要新增一个bool数组来存储是否访问过某数，
    因此在递归的条件中除了要考虑值是否满足以外，还需要考虑是否访问过该数

    dfs可以用递归版的也可以不用非递归版
    递归版是用系统栈，压入了所有的信息
    非递归版是自己构造stack，压入相关信息
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None or board == []:
            return 0
        m, n = len(board), len(board[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board