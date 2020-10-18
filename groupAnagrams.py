#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 11:10 上午
# @Author  : lambert
# @Site    : 
# @File    : groupAnagrams.py
# @Software: PyCharm
# class Solution:
#     def groupAnagrams(self, strs):
#         # n = len(strs)
#         def permute(nums: list):
#             # def gen_permute(nums:list):
#             if len(nums) == 1:
#                 return [nums]
#             results = []
#             for i in range(len(nums)):
#                 res = permute(nums[:i] + nums[i + 1:])
#                 for r in res:
#                     r.append(nums[i])
#                     results.append(r)
#             return results
#         i = 0
#         res = []
#         if strs == [""]:
#             return [[""]]
#         kong = []
#         while i < len(strs):
#             ss = []
#             if strs[i] == "":
#                 kong.append("")
#                 i+=1
#             else:
#                 permutes = permute(list(strs[i]))
#                 for p in permutes:
#                     s = "".join(p)
#                     if s in strs:
#                         ss.append(s)
#                         strs.remove(s)
#                 res.append(ss)
#         if len(kong) >0 :
#             res.append(kong)
#         return res
class Solution:
    def groupAnagrams(self, strs):
        dd = {}
        for i in range(len(strs)):
            ss = "".join(sorted(strs[i]))
            if ss not in dd:
                dd[ss] = [strs[i]]
            else:
                dd[ss].append(strs[i])
        return list(dd.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

# print(Solution().permute())
