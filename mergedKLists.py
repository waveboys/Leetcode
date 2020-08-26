#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/25 下午2:07
#@Author: guangliang
#@File  : mergedKLists.py
# Definition for singly-linked list.
"""
解题思路：暴力求解，依次比较两个链表，并进行合并，报错超时
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        def mergeTwoLists(l1,l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1,l2.next)
                return l2
        n = len(lists)
        if n==0:
            return None
        l = lists[0]
        for i in range(1,n):
            l = mergeTwoLists(l,lists[i])
        return l

class Solution1:
    def mergeKLists(self, lists):
        def mergeTwoLists(l1,l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1,l2.next)
                return l2
        n = len(lists)
        if n==0:
            return None
        l = lists[0]
        for i in range(1,n):
            l = mergeTwoLists(l,lists[i])
        return l

# 测试
l1 = ListNode(val=1)
l1.val = 1
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(6)
l2 = ListNode(val=1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(7)
lists = [l1,l2]

l3 = ListNode(val=2)
l3.next = ListNode(3)
l3.next.next = ListNode(8)
l3.next.next.next = ListNode(9)
lists = [l1,l2,l3]
l = Solution().mergeKLists(lists)
while l:
    print(l.val)
    l = l.next
# print(l.val)

