#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/21 下午8:59
#@Author: guangliang
#@File  : searchRange.py
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
"""
1、基础版，采用二分查找方法+递归方法依次找到最大和最小的索引,这题需要注意当目标值等于中间值的时候，需要分别递归查找左半部分和右半部分
   1.1 对整个数组采用二分查找法判断目标值在左半部分，还是在又半部分
   1.2 如果中间值刚才等于目标值的话，则需要分别递归二分查找左半部分和右半部分的数组。
   1.3 如果目标值大于nums[mid],则left = mid + 1,如果目标值小于nums[mid],则right = mid -1
"""
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        n = len(nums)
        if n <1:
            return [-1,-1]
        left = 0
        right = n-1
        res = []
        def findRange(nums,left,right):
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    res.append(mid)
                    if mid+1 <= right and target == nums[mid+1]:
                        res.append(mid+1)
                        findRange(nums,mid+2,right)
                    if mid-1>=left and target == nums[mid-1]:
                        res.append(mid-1)
                        findRange(nums,left,mid-2)
                    break
                elif target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        findRange(nums,left,right)
        if res == []:
            return [-1,-1]
        else:
            return [min(res),max(res)]
"""
2、优化方法：分别从头部和尾部开始遍历，从头部开始遍历找到的第一个就是start。从尾部开始遍历，找到的第一个就是end
"""
class Solution1:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]
print(Solution().searchRange([5,7,7,8,8,10],6))

