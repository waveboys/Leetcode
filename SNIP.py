#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/19 下午3:12
#@Author: guangliang
#@File  : SNIP.py
# Definition for singly-linked list.
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
回溯法，先把最后的两个交换，然后交换前面的
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head.next
        head.next = self.swapPairs(head.next.next)
        p.next = head
        return p
