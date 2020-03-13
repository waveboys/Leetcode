#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/13 上午10:29
#@File  : Longest_Common_Prefix.py
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
"""
找出最长前缀，首先需要找出最短字符串的长度，然后遍历每个字符串，依次比较每个字符
"""
class Solution:
    def longestCommonPrefix(self, strs: list):
        common_str = strs[0] if strs else ""
        end_flag = len(common_str)
        for i in range(1,len(strs)):
            if len(strs[i]) < end_flag:
                end_flag = len(strs[i])
            for j in range(end_flag):
                if strs[i][j] != common_str[j]:
                    end_flag = j
                    break
        return common_str[:end_flag]

