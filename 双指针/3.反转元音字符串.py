# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 14:56
# @Author  : xiaoqing
# @File    : 3.反转元音字符串.py
# @Software: PyCharm Community Edition

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    l, r = 0, len(s) - 1
    list_str = [''] * len(s)
    list_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while l <= r:
        if s[l] not in list_vowels:
            list_str[l] = s[l]
            l += 1
        elif s[r] not in list_vowels:
            list_str[r] = s[r]
            r -= 1
        else:
            list_str[l] = s[r]
            list_str[r] = s[l]
            l += 1
            r -= 1
    res = ''
    for i in list_str:
        res += '' + i
    return res
r = reverseVowels("hello")
print(r)