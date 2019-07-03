# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 15:56
# @Author  : xiaoqing
# @File    : 6.判断是否有环.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l, r = head, head
        if head == None:
            return False
        while l.next != None and r.next and r.next.next != None:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False