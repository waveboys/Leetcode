#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/14 上午1:38
#@Author: guangliang
#@File  : Sum_Two_Integers.py
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        print(b&mask)
        while b & mask:
            a, b = a^b, (a&b) << 1
        return a & mask if b > mask else a

print(Solution().getSum(3,-2))
