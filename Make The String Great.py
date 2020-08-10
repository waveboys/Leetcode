#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/9 上午10:31
#@Author: guangliang
#@File  : Make The String Great.py
"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
"""
class Solution:
    def makeGood(self, s):
        if s == "":
            return ""
        # def back_trick(s:str):
        i = 0
        # n = len(s)
        while i<len(s)-1:
            if s[i] != s[i+1] and (s[i] == s[i+1].lower() or s[i].lower()==s[i+1]):
                s = s.replace(s[i]+s[i+1],"")
                i=0
            else:
                i+=1
        return s
print(Solution().makeGood("Pp"))
