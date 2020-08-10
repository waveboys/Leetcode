#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/9 上午10:57
#@Author: guangliang
#@File  : findKthBit.py

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        d=["0","011","0111001","011100110110001"]
        if n<=len(d):
            return d[n-1][k-1]
        for i in range(4,n):
            s = d[i-1] + "1"
            invert = ""
            if k<=len(d[i-1]):
                return d[i-1][k-1]
            for j in range(len(d[i-1])):
                if d[i-1][j] == "0":
                    invert += "1"
                else:
                    invert += "0"
            d.append(s+invert[::-1])
        print()
        return d[n-1][k-1]
print(Solution().findKthBit(9,1))