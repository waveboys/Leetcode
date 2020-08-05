#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/5 上午10:44
#@Author: guangliang
#@File  : countAndSay.py
"""
解题思路：需要遍历求出5到n之间每一个数的对应的字符串
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        say_d = {1:"1",2:"11",3:"21",4:"1211",5:"111221"}
        if n<=5:
            return say_d[n]
        i=5
        while i<=n:
            fs = ""
            ss = say_d[i]
            count = 1
            for j in range(len(ss)):
                if (j+1) < len(ss) and ss[j] == ss[j+1]:
                    count +=1
                else:
                    fs += str(count) + ss[j]
                    count=1
            # if ss[-1] != ss[-2]
            i += 1
            say_d[i] = fs
        return say_d[n]
print(Solution().countAndSay(5))
# 6 312211