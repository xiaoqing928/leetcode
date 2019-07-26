# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 11:01
# @Author  : xiaoqing
# @File    : 7链表求和.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        sum1 = str(int(num1) + int(num2))
        l = ListNode(sum1[0])
        head = l
        for i in sum1[1:]:
            l.next = ListNode(i)
            l = l.next
        return head