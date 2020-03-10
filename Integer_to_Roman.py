#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/10 上午11:09
#@File  : Integer_to_Roman.py
import enum

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
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    """
    比较笨的方法,通过if一步一步判断
    """
    def intToRoman(self, num: int):
        symbol = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        num_100 = num % 1000
        num_10 = num % 100
        num_1 = num % 10
        num_1000 = num - num_100
        s = ""
        if num_1000 >0:
            n_1000 = num_1000 // 1000
            s += n_1000 * symbol[1000]
        if num_100 >0:
            n_100 = (num_100-num_10) // 100
            if n_100<4:
                s += n_100 * symbol[100]
            elif n_100==4:
                s += "C" + symbol[500]
            elif n_100<9:
                s += symbol[500] + (n_100-5)*symbol[100]
            else:
                s +=  symbol[100]+symbol[1000]
        if num_10 > 0:
            n_10 = (num_10-num_1) // 10
            if n_10 <4:
                s += n_10 * symbol[10]
            elif n_10==4:
                s += symbol[10] + symbol[50]
            elif n_10 < 9:
                s += symbol[50] + (n_10-5)*symbol[10]
            else:
                s += symbol[10] + symbol[100]
        if num_1 > 0:
            if num_1 <4:
                s += num_1*symbol[1]
            elif num_1 == 4:
                s += symbol[1]+symbol[5]
            elif num_1 <9:
                s += symbol[5] + (num_1-5)*symbol[1]
            else:
                s += symbol[1] + symbol[10]
        return s
class Roman(enum.Enum):
    M = 1000
    CM = 900
    D = 500
    CD = 400
    C = 100
    XC = 90
    L = 50
    XL = 40
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1

class Solution1:
    """
    比较灵活的做法
    """
    def intToRoman(self, num: int) -> str:
        result = []
        for _ in Roman:
            result += _.name * (num // _.value),
            num %= _.value
        return ''.join(result)
print(Solution1().intToRoman(1994))