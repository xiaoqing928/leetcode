# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 9:58
# @Author  : xiaoqing
# @File    : 4删除重复节点.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        curhead, nexthead = head, head.next
        while curhead and nexthead:
            if curhead.val == nexthead.val:
                curhead.next = nexthead.next
                nexthead = nexthead.next
            else:
                curhead = curhead.next
                nexthead = nexthead.next
        return head