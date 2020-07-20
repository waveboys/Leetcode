#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/20 下午8:36
#@Author: guangliang
#@File  : search.py
"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

"""
解题思路：
1、从题目要求的时间限制，就可以知道这道题是二分查找问题。因此需要在旋转后的数组里面使用二分查找来解决这个问题
2、二分搜索的关键是确定目标值在哪一半的数据里，因此需要确定目标址在哪一半的数组里。
3、这个是[0,1,2,4,5,6,7]做各种旋转后的数组：
0　　1　　2　　 4　　5　　6　　7

7　　0　　1　　 2　　4　　5　　6

6　　7　　0　　 1　　2　　4　　5

5　　6　　7　　 0　　1　　2　　4

4　　5　　6　　7　　0　　1　　2

2　　4　　5　　6　　7　　0　　1

1　　2　　4　　5　　6　　7　　0
从这些旋转后的数据来看，旋转后的数组里，左半边或者右半边总有一边是有序的。同时从这几个数组里面还可以发现：
（1）当最左边的数据小于等于中间数据时，左半边是有序的
 (2)当最左边的数据大于中间数据时，右半边是有序的
"""
class Solution:
    def search(self, nums: list, target: int) -> int:
        n = len(nums)
        if n<1:
            return -1
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
print(Solution().search([3,1],1))