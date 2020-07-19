#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/14 下午2:40
#@Author: guangliang
#@File  : nextPermutation.py
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
# class Solution:
#     def nextPermutation(self, nums: list) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         flag=False
#         for i in range(n-1,0,-1):
#             if nums[i] > nums[i-1]:
#                 temp = nums[i]
#                 nums[i] = nums[i-1]
#                 nums[i-1] = temp
#                 flag=True
#                 break
#         if flag==False:
#             nums.sort()
#         print(nums)

"""
/** Tips: next permuation based on the ascending order sort
 * sketch :
 * current: 3   7  6  2  5  4  3  1  .
 *                    |  |     |     |
 *          find i----+  j     k     +----end
 * swap i and k :
 *          3   7  6  3  5  4  2  1  .
 *                    |  |     |     |
 *               i----+  j     k     +----end
 * reverse j to end :
 *          3   7  6  3  1  2  4  5  .
 *                    |  |     |     |
 *          find i----+  j     k     +----end
 A = [3,7,6,2,5,4,3,1]
 (1) 从后向前找第一个相邻元素(i,j),并且满足A[i]<A[j]，例如(3,4),由此可知从(j,end)都是降序排列的。
 (2) 在(j,end)里面找出一个最小的k使A[k]>A[i],由于(j,end)是降序的，所以必然存在一个k使得A[k]>A[i]所以从后向前查找
 第一个满足A[k]>A[i]的k。
 (3) 将i对应的值与k对应的值进行交换，因为下一个全排列必须是当前排列按照升续相邻的排列，故选择最小的元素替换i。
 交换后的[j,end] 仍然是降序的。因为在(k,end) 中必然小于i的值，而在(j,k)中必然大于k的值，并且大于i。
 (4) 交换后的(j,end)是降序的，因此需要转置下顺序。
"""


def nextPermutation(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n<2:
        return nums
    i = n-1
    j = i
    while i>0 and nums[i]<nums[i-1]:
        i-=1
    if i==0:
        return nums.reverse()
    i-= 1
    while j>i and nums[j]<nums[i]:
        j -= 1
    nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = nums[:i:-1]
    return nums


print(nextPermutation([3,7,6,2,5,4,3,1]))