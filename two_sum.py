#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/12 下午10:55
#@Author: guangliang
#@File  : two_sum.py
"""
采用字典查找
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in d:
                return [d[target - numbers[i]] + 1, i + 1]
            d[numbers[i]] = i
