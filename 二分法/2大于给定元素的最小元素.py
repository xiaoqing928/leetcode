# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 9:25
# @Author  : xiaoqing
# @File    : 2大于给定元素的最小元素.py
# @Software: PyCharm Community Edition

'''
题目描述：给定一个有序的字符数组 letters 和一个字符 target，
要求找出 letters 中大于 target 的最小字符，
如果找不到就返回第 1 个字符。
'''

def nextGreatestLetter(letters, target):
    l, r = 0, len(letters) - 1
    while l <= r:
        mid = int(l + (r - l) / 2)
        if letters[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    if l < len(letters):
        return letters[l]
    return letters[0]
letters = ["c", "f", "j"]
target = "k"
print(nextGreatestLetter(letters, target))