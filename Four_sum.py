#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/15 下午10:06
#@Author: guangliang
#@File  : Four_sum.py
"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
"""
"""
解法：在3sum的基础上再加一层循环，相当与有2个for循环依次遍历，然后两个指针从最左边和最右边开始遍历
"""
from itertools import combinations
class Solution:
    def fourSum(self, nums: list, target: int):
        ans = []
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        for i in range(n-3):
            a = nums[i]
            for j in range(i+1,n-2):
                b = nums[j]
                left = j+1
                right = n-1
                while left < right:
                    s = a + b + nums[left] + nums[right]
                    if s == target:
                        ans.append([a,b,nums[left],nums[right]])
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
        for i in range(len(ans)-1):
            j = i+1
            while j < len(ans):
                if ans[i][0] == ans[j][0] and ans[i][1] == ans[j][1] and ans[i][2] == ans[j][2] \
                    and  ans[i][3] == ans[j][3]:
                    ans.pop(j)
                else:
                    j += 1
        return ans

    def fourSum1(self, nums: list, target: int):
        c = list(sorted(set(combinations(nums, 4))))
        s = map(sum, c)
        r = (zip(c, s))
        ans = (list(map(list, [sorted(i[0]) for i in (filter(lambda x: x[1] == target, r))])))
        for i in range(len(ans)-1):
            j = i+1
            while j < len(ans):
                # a = sorted(ans[i])
                # b = sorted(ans[j])
                if ans[i][0] == ans[j][0] and ans[i][1] == ans[j][1] and ans[i][2] == ans[j][2] \
                    and  ans[i][3] == ans[j][3]:
                    ans.pop(j)
                else:
                    j += 1
        return ans
print(Solution().fourSum1([-5,5,4,-3,0,0,4,-2],4))
