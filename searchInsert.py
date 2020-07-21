#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/21 下午10:11
#@Author: guangliang
#@File  : searchInsert.py
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
"""
1、二分查找，如果刚才等于中间值，则返回中间值的索引。
2、如果大于中间值，且小于中间值后一位，则返回mid+1
3、如果小于中间值，且大于中间值前一位，则返回mid
"""
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            if target <=nums[0]:
                return 0
            else:
                return 1
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if mid-1 >= left and nums[mid-1]<target:
                    return mid
                else:
                    right = mid-1
            else:
                if mid+1 <= right and nums[mid+1] > target:
                    return mid+1
                else:
                    left = mid+1
        if left>right and right==-1:
            return 0
        if left > right and left== n:
            return n
print(Solution().searchInsert([1,3,5,6],5.5))


