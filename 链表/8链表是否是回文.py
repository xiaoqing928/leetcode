# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 11:33
# @Author  : xiaoqing
# @File    : 8链表是否是回文.py
# @Software: PyCharm Community Edition

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        #计算长度
        cnt = 0
        head1 = head
        while head1:
            cnt += 1
            head1 = head1.next
        cur = head
        #移位
        import math
        nums = math.ceil(cnt / 2)
        for i in range(nums):
            head = head.next
        newhead = None
        #反转链表
        while head:
            head.next, newhead, head = newhead, head, head.next
        while newhead and cur:
            if newhead.val != cur.val:
                return False
            newhead = newhead.next
            cur = cur.next
        return True
list = [1, 1, 2, 1]
head = ListNode(list[0])
l = head
for i in list[1:]:
    head.next = ListNode(i)
    head = head.next
print(l.next.val)
a = Solution()
r = a.isPalindrome(l)
print(r)