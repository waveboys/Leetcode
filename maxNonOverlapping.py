#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/9 上午11:27
#@Author: guangliang
#@File  : maxNonOverlapping.py
"""
Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
Example 3:

Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3
Example 4:

Input: nums = [0,0,0], target = 0
Output: 3
"""
class Solution:
    def maxNonOverlapping(self, nums, target: int):
        res = total = 0
        d, last = {0: -1}, -1
        for i, v in enumerate(nums):
            total += v
            if total - target in d and d[total - target] >= last:
                res += 1
                last = i
            d[total] = i
        return res
print(Solution().maxNonOverlapping([-2,6,6,3,5,4,1,2,8],10))