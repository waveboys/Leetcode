#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/8 下午6:29
#@Author: guangliang
#@File  : threeSumClosest.py
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        result = nums[0]+nums[1]+nums[n-1]
        diff = abs(result-target)
        for i in range(0,n-1):
            left = i+1
            right = n - 1
            while left < right:
                s = nums[left] + nums[i] + nums[right]
                new_diff = abs(s-target)
                if new_diff < diff:
                    diff = new_diff
                    result = s
                if s<target:
                    left = left + 1
                else:
                    right = right -1
        return result