# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 10:03
# @Author  : xiaoqing
# @File    : 1链表相交节点.py
# @Software: PyCharm Community Edition

'''
    链表的题就像是送分题，逻辑还是比较简单的，仔细分析就好
    这个题先找到链表的长度，然后做差，得到差值
    较长的链表先移动"差值"长度的距离，接着就可以比较
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1, cur2 = headA, headB
        l1 , l2 = 0, 0
        if headA == None or headB == None:
            return None
        while headA.next:
            headA = headA.next
            l1 += 1
        while headB.next:
            headB = headB.next
            l2 += 1
        if l1 >= l2:
            for i in range(l1 - l2):
                cur1 = cur1.next
        else:
            for i in range(l2 - l1):
                cur2 = cur2.next
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None