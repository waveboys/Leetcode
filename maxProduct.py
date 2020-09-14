#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/14 上午10:28
#@Author: guangliang
#@File  : maxProduct.py
"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""
class Solution:
    def maxProduct(self, words):
        n = len(words)
        max_product = 0
        for i in range(n-1):
            for j in range(i+1,n):
                n1 = len(words[i])
                n2 = len(words[j])
                if len(set(words[i]) & set(words[j]))>0:
                    continue
                if n1*n2 > max_product:
                    max_product = n1*n2
        return max_product
print(Solution().maxProduct(["a","aa","aaa","aaaa"]))
