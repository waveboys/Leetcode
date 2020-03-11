#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/11 上午11:43
#@File  : Roman_to_integer.py
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

"""
"""
把罗马字符转换为整数，主要是要注意4 9 40 90 400 900 之类的罗马字符转换，
"""
class Solution:
    def romanToInt(self, s: str):
        symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,
                  "XC":90,"CD":400,"CM":900}
        last_str = s[0]
        last_num = symbol[last_str]
        sum_n = last_num
        for i in range(1,len(s)):
            new_num = symbol[s[i]]
            if new_num > last_num:
                sum_n += new_num -2*last_num   # 如果前面一个字符对应的数字小于当前字符对应的数字，则做减法运算
            else:
                sum_n += new_num
            last_num = new_num
        return sum_n


