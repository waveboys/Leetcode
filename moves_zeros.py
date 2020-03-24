#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/23 上午10:30
#@Author: guangliang
#@File  : moves_zeros.py
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        zero_nums = 0
        i=0
        while i < len(nums):
            if nums[i]==0:
                zero_nums += 1
                nums.pop(i)
            else:
                i += 1
        for j in range(zero_nums):
            nums.append(0)
print(Solution().moveZeroes([0,1,0,3,12]))