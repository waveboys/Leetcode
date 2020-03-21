#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/21 下午5:35
#@Author: guangliang
#@File  : RNIK.py
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

"""
思路：每次翻转k个节点，则需要知道有多少个这样的k,在当前k个节点和下一个k个节点做好衔接。
主要分为两部分：
1、找到需要翻转的部分。
2、实现对k个节点的翻转，
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, K: int) -> ListNode:
        if not head:
            return None
        nxt = head.next
        n = 1
        while nxt:
            n += 1
            nxt = nxt.next
        n //= K
        def reverseKNode(node,k,g,pa):
            if not node or not g:
                return node
            if k==K:
                nxt = node.next
                pa.next = reverseKNode(nxt, 1, g-1, nxt)
                return node
            nxt = node.next
            nhead = reverseKNode(nxt,k+1,g,pa)
            nxt.next = node
            return nhead
        return reverseKNode(head,1,n,head)