#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/7 下午6:52
#@Author: guangliang
#@File  : combinationSum2.py
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        def back_trick(candidates,target,r,k,s):
            if s==target:
                res.append(r[:])
            for i in range(k,len(candidates)):
                temp = candidates[i]
                if s + temp> target:
                    break
                # 当第二次出现重复数字时，且不是在回溯的起始位置时，直接跳过
                if i>k and candidates[i] == candidates[i-1]:
                    continue
                s += temp
                r.append(temp)
                back_trick(candidates,target,r,i+1,s)   # i+ 1避免重复加上自身
                r.pop()
                s -= temp
        candidates.sort()
        back_trick(candidates,target,[],0,0)
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5],8))

