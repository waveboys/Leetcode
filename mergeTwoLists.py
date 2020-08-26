#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/25 下午1:56
#@Author: guangliang
#@File  : mergeTwoLists.py
# Definition for singly-linked list.
"""合并两个有序的链表"""
"""
解题思路：采用递归的方法，依次合并l1和l2的每个元素，当l1的当前值小于l2的当前值时，
把l1 的下一个值和l2的当前值进行比较。因此把l1.next 和l2 递归下去。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 测试
l1 = ListNode(x=1)
l1.val = 1
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(6)
l2 = ListNode(x=1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(7)
l = Solution().mergeTwoLists(l1,l2)
while l:
    print(l.val)
    l = l.next