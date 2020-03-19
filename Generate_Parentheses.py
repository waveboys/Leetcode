#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/18 下午3:58
#@Author: guangliang
#@File  : Generate_Parentheses.py
"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

"""递归解决，有点绕，暂时没有理解透"""
class Solution:
    def generateParenthesis(self, n):

        lst = [''] * (2 * n)
        res = []

        def helper(lst, idx, n, beg, end):
            if end == n:
                res.append(''.join(lst))
            else:
                if beg < n:
                    lst[idx] = "("
                    helper(lst, idx + 1, n, beg + 1, end)
                if end < beg:
                    lst[idx] = ")"
                    helper(lst, idx + 1, n, beg, end + 1)

        helper(lst, 0, n, 0, 0)
        return res
print(Solution().generateParenthesis(3))