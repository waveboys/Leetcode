#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/24 下午2:28
#@Author: guangliang
#@File  : strStr.py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
print(Solution().strStr("",""))

