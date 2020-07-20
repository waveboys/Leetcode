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
"""
解题思路：对于这种括号匹配的问题，首先想到的就是采用堆栈的思想，遇到左括号的时候进堆栈，遇到有括号的时候出堆栈。
1、采用start 来记录遇到的第一个完整的左括号
2、每遇到一个"("的时候，把这个左括号添加到列表中
3、遇到")"时，则判断当前列表是否为空。如果为空的话，则重新给start赋值。
如果栈不为空，则将栈顶元素取出，此时若栈为空，则更新结果和 i - start + 1 中的较大值，
否则更新结果和 i - st.top() 中的较大值
参考：https://www.cnblogs.com/grandyang/p/4424731.html
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
                    start = i+1   # 重新设定start的值
                else:
                    stack.pop()
                    if stack == []:
                        res = max(res,i-start+1)
                    else:
                        res = max(res,i-stack[-1])
        return res

print(Solution().longestValidParentheses(")()())"))

