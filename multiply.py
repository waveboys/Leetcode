#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/17 下午9:41
#@Author: guangliang
#@File  : multiply.py
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m,n=len(num1),len(num2)
        num1,num2=list(reversed(num1)),list(reversed(num2))
        p = [0 for k in range(m + n)]
        for i in range(m):
           shi_wei = 0
           for j in range(n):
               temp = (ord(num1[i])-ord("0")) * (ord(num2[j])-ord("0"))
               temp = temp + shi_wei + p[i+j]
               shi_wei = temp // 10
               p[i+j] = temp % 10
           p[i+j+1] = shi_wei
        res = ""
        p = list(reversed(p))
        for i in range(0,m+n):
            if p[i] != 0:
                break
        for j in range(i,m+n):
            res += str(p[j])
        return res
print(Solution().multiply("123","456"))