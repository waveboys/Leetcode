#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 12:27 上午
# @Author  : lambert
# @Site    : 
# @File    : permuteUnique.py
# @Software: PyCharm

"""
采用DFS深度遍历
"""
class Solution:
    def permuteUnique(self, nums: list):
        if len(nums) == 1:
            return [nums]
        results = []
        flag = []
        for i in range(len(nums)):
            if nums[i] in flag:
                continue
            flag.append(nums[i])
            res = self.permuteUnique(nums[:i] + nums[i + 1:])
            for r in res:
                r.append(nums[i])
                results.append(r)
        return results
print(Solution().permuteUnique([3,3,0,3,3]))