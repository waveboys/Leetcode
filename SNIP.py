#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/19 下午3:12
#@Author: guangliang
#@File  : SNIP.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head.next
        head.next = self.swapPairs(head.next.next)
        p.next = head
        return p
