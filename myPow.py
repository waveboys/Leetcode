#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 5:37 下午
# @Author  : lambert
# @Site    : 
# @File    : myPow.py
# @Software: PyCharm
"""
求解思路很简单，采用递归的思想就可以不解决，但是需要注意复杂度。
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0:
            return 0
        if n<0:
            return 1.0/self.myPow(x,-n)
        if n % 2:
            return self.myPow(x,n-1)*x
        p = self.myPow(x,n//2)
        return p*p

print(Solution().myPow(2,4))