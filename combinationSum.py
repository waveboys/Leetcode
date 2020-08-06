#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/5 下午8:24
#@Author: guangliang
#@File  : combinationSum.py
#解题思路：回溯的思想,

class Solution:
    def back_track(self,candidates,target,r,s,i):
        if s==target:  # 若是求和等于目标的话，就把结果列表加进来
            self.res.append(r[:])
        for j in range(i,len(candidates)):
            temp = candidates[j]
            if s + temp > target:
                break
            s += temp
            r.append(temp)
            # 对于每个新加进来的都回溯一遍
            self.back_track(candidates,target,r,s,j)
            r.pop()
            s -= temp

    def combinationSum(self, candidates: list, target: int):

        self.res = []
        if len(candidates) < 1:
            return []
        candidates.sort()
        self.back_track(candidates,target,[],0,0)
        return self.res

print(Solution().combinationSum([1,2,4,5,6,7],7))