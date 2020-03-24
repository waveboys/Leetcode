#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/24 下午2:44
#@Author: guangliang
#@File  : DTI.py
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        if dividend == 0:
            return 0

        if divisor == 1:
            return dividend
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        s = 0
        while dividend >= divisor:
            len1 = len(str(dividend))
            len2 = len(str(divisor))
            diff = len1 - len2
            ss = 1
            if diff >= 1:
                if divisor*pow(10,diff) <= dividend:
                    ss = pow(10,diff)
                else:
                    ss =pow(10,diff-1)
            s += ss
            dividend -= divisor*ss
        return sign * s
print(Solution().divide(2147483648,1))