# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 10:04
# @Author  : xiaoqing
# @File    : 9链表分成k个相近的部分.py
# @Software: PyCharm Community Edition

list1 = [[] for i in range(3)]
list1[0].append(1)
list1

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # 取长度
        cur = root
        count = 0
        while cur:
            count += 1
            cur = cur.next

        # 分区中的数量和多出来的数量
        parts = int(count / k)
        add = count % k

        cur = root
        pre = None
        list1 = [None for i in range(k)]
        for i in range(k):
            if cur == None:
                list1[i] = []
            else:
                list1[i] = cur
                if add > 0:
                    for i in range(parts + 1):
                        pre = cur
                        cur = cur.next
                if pre != None:
                    pre.next = None
                add -= 1
        return list1