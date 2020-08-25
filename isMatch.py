#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/18 上午10:13
#@Author: guangliang
#@File  : isMatch.py
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
"""
"""
解题思路：动态规划问题
"""
class Solution:
    def isMatch(self, s: str, p: str, tab=None) -> bool:
        if not p:
            return not s
        if not s:
            return all(c == '*' for c in p)
        if not tab:
            tab = [[-1 for _ in range(len(p)+1)]
                   for _ in range(len(s)+1)]
        if tab[len(s)][len(p)] is not -1:
            return tab[len(s)][len(p)]
        result = False
        if s[0] == p[0] or p[0] == '?':
            result = self.isMatch(s[1:], p[1:], tab=tab)
        elif p[0] == '*':
            result = (self.isMatch(s, p[1:], tab=tab) or
                      self.isMatch(s[1:], p, tab=tab) or
                      self.isMatch(s[1:], p[1:], tab=tab))
        tab[len(s)][len(p)] = result

        return result
print(Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
"***bba**a*bbba**aab**b"))


