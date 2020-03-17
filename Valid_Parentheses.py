#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/17 下午1:44
#@Author: guangliang
#@File  : Valid_Parentheses.py
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
"""
使用堆栈，当出现有左边的符号时，加入堆栈，当出险右边的符号时，pop出堆栈进行匹配。
注意空的情况，最后还要判断堆栈是否为空
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        if n%2:
            return False
        ss = []
        # ss.append(s[0])
        if s[0] in [")","}","]"]:
            return False
        ss.append(s[0])
        for i in range(1,n):
            if s[i] in ["(","{","["]:
                ss.append(s[i])
            else:
                p_s = ss.pop()
                if p_s + s[i] in ["()","{}","[]"]:
                    continue
                else:
                    return False
        if len(ss)==0:
            return True
        else:
            return False
print(Solution().isValid("(("))

