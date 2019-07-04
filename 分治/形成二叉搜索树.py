# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 11:04
# @Author  : xiaoqing
# @File    : 形成二叉搜索树.py
# @Software: PyCharm Community Edition

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        if n < 1:
            return []
        return self.generateTree(1, n)

    def generateTree(self, s, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if s > n:
            res.append(None)
        for i in range(s, n + 1):
            left = self.generateTree(s, i - 1)
            right = self.generateTree(i + 1, n)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res

a = Solution()
a.generateTrees(3)