# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 10:30
# @Author  : xiaoqing
# @File    : 2反转链表.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = None
        while head:
            # 反转 移位 就ok
            head.next, newhead, head = newhead, head, head.next
        return newhead