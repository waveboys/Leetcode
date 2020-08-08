#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/8 下午2:20
#@Author: guangliang
#@File  : firstMissingPositive.py
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
"""
"""
思路1： 这道题让我们找缺失的首个正数，由于限定了 O(n) 的时间，所以一般的排序方法都不能用，最开始博主没有看到还限制了空间复杂度，所以想到了用 HashSet 来解，这个思路很简单，把所有的数都存入 HashSet 中，然后循环从1开始递增找数字，
哪个数字找不到就返回哪个数字，如果一直找到了最大的数字（这里是 nums 数组的长度
"""
class Solution:
    def firstMissingPositive(self, nums):
        if len(nums)<1:
            return 1
        nums = list(set(nums))
        nums.sort()
        min_num = nums[0]
        max_num = nums[-1]
        if min_num>1 or max_num<0:
            return 1
        gen_nums = 1
        n_nums = len(nums)
        for i in range(n_nums):
            if nums[i]<=0:
                continue
            if nums[i] > gen_nums:
                return gen_nums
            gen_nums += 1
        return gen_nums
# 思路二： 直接判断从1开始的整数是否在nums里面就好了
    def firstMissingPositive1(self, nums: List[int]) -> int:
        count = 1
        while True:
            if count not in nums:
                return count
            count += 1
print(Solution().firstMissingPositive([-10,1,2,3,4]))