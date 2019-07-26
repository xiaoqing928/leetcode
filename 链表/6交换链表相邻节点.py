# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 10:42
# @Author  : xiaoqing
# @File    : 6交换链表相邻节点.py
# @Software: PyCharm Community Edition

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0) # previous before head
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            temp = head.next
            head.next = temp.next
            temp.next = head.next.next
            head.next.next = temp
            head = temp
        return dummy.next