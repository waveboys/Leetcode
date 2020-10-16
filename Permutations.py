#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 12:06 上午
# @Author  : lambert
# @Site    : 
# @File    : Permutations.py
# @Software: PyCharm
class Solution:
    def permute(self, nums: list):
        # def gen_permute(nums:list):
        if len(nums) == 1:
            return [nums]
        results = []
        for i in range(len(nums)):
            res=self.permute(nums[:i] + nums[i+1:])
            for r in res:
                r.append(nums[i])
                results.append(r)
        return results
        # return  gen_permute(nums)
print(Solution().permute([1,2,3]))


