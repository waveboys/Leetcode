#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/16 下午6:16
#@Author: guangliang
#@File  : longestValidParentheses.py

"""
Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start = 0
        res = 0
        stack = []
        n = len(s)
        if n<2:
            return 0
        for i in range(0,n):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack == []:
                    start = i+1
                else:
                    stack.pop()
                    if stack == []:
                        res = max(res,i-start+1)
                    else:
                        res = max(res,i-stack[-1])
        return res

print(Solution().longestValidParentheses(")()())"))

