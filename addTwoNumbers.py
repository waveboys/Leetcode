#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/14 上午1:15
#@Author: guangliang
#@File  : addTwoNumbers.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            return l1
        temp = 0
        val = l1.val + l2.val
        if val>=10:
            temp = 1
            val = val-10
        head = ListNode(val)
        l1 = l1.next
        l2 = l2.next
        l=head
        while l1 and l2:
            val = l1.val + l2.val + temp
            if val >= 10:
                temp=1
                val = val-10
            else:
                temp=0
            node = ListNode(val)
            l.next = node
            l = l.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val
            val = val + temp
            if val >= 10:
                temp = 1
                val -= 10
            else:
                temp = 0
            node = ListNode(val)
            l.next = node
            l = l.next
            l1 = l1.next
        while l2:
            val = l2.val
            val = val + temp
            if val >= 10:
                temp = 1
                val -= 10
            else:
                temp = 0
            node = ListNode(val)
            l.next = node
            l = l.next
            l2 = l2.next
        if temp==1:
            l.next = ListNode(temp)
        return head
l1 = ListNode(5)
l1_1 = ListNode(4)
l1_2 = ListNode(7)
l1.next = l1_1
l1_1.next = l1_2
l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2
l = Solution().addTwoNumbers(l1,l2)
while l:
    print(l.val)
    l = l.next