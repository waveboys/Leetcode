#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/11 上午10:59
#@Author: guangliang
#@File  : trap.py
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

"""
解题思路：两高夹一矮才能存到水。因此，每一坐标i上存多少水是由 1.其自身高度 2.它左边的最高高度left_most 
3.它右边的最高高度right_most三种因素决定的。
只有当当前位置的高度小于左边和右边高度时，才可能存到水。需要同时考虑左边和右边的高度

"""
class Solution:
    def trap(self, height: list[int]) -> int:  # O(N) + O(1)
        left_max, right_max = 0, 0
        start, end, ans = 0, len(height) - 1, 0

        while (start < end):

            if height[start] < height[end]:
                if height[start] > left_max:
                    left_max = height[start]
                else:
                    ans += left_max - height[start]
                start += 1
            else:
                if height[end] > right_max:
                    right_max = height[end]
                else:
                    ans += right_max - height[end]
                end -= 1

        return ans

