# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:14
# @Author  : xiaoqing
# @File    : 10奇偶顺序排序.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur, nextcur = head, head.next
        evenhead = head.next
        while nextcur and nextcur.next:
            cur.next = nextcur.next
            nextcur.next = nextcur.next.next
            cur = cur.next
            nextcur = nextcur.next
        cur.next = evenhead
        return head