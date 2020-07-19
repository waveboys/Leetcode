#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/13 上午9:25
#@Author: guangliang
#@File  : findSubStr.py
"""
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
"""
解题思路：这是一个窗口移动问题，
解这道题的关键对我而言是用words 去匹配s,还是用s里的单个单词的长度去匹配words列表里的每个单词,、
就是确定移动哪个窗口

"""
import collections
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        soulution = []
        m = len(words)
        if m==0:
            return []
        world_len = len(words[0])

        word_dict = collections.Counter(words)

        for i in range(len(s)-m*world_len+1):  #因为最后一个能匹配上的一定有m*world_len的长度，所以要减去m*world_len 的长度
            temp_word_dict = word_dict.copy()
            # 有多少个单词就匹配多少次
            for j in range(m):
                new_words = s[i+j*world_len:i+j*world_len+world_len] # 取出一个单词长度的字符串
                if new_words in temp_word_dict:
                    # 判断该单词出现次数是否大于1，如果出现次数大于1，则减去1次，否则把这个单词去掉，不需要再匹配这个单词了
                    if temp_word_dict[new_words] > 1:
                        temp_word_dict[new_words] -= 1
                    else:
                        temp_word_dict.pop(new_words)
                else:
                    break

                if not temp_word_dict:
                    soulution.append(i)

        return soulution
s = "wordgoodgoodgoodbestword",
words = ["word","good","best","word"]
print(Solution().findSubstring(s,words))